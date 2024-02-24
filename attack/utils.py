from openai_cost_tracker import query_openai
import time
import os
import json
import openai
from collections import defaultdict


def api_key_setup(model):
    if model.__contains__("gpt"):
        openai.api_key = open("/home/users/rx55/projects/keys/duke_math_key.txt", "r").read()


def save(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def generate_prompt(problem):

    return f'Solve a math problem. The solution ends with "the answer is (a number)" like "the answer is 1".\nQuestion: {problem}\nAnswer: Let\'s think step by step.'

def get_completion(prompt, model_name, hf_model=None, hf_tokenizer=None, simulation=False):
    if "gpt" not in model_name:

        model_inputs = hf_tokenizer([prompt], return_tensors="pt").to('cuda')

        generated_ids = hf_model.generate(**model_inputs, max_new_tokens=512, do_sample=True, temperature=0.1)

        res = hf_tokenizer.batch_decode(generated_ids)[0]

        return res

    # call openai apis
    else:
        MAX_RETRIES = 10
        errors = 0  # Count consecutive errors

        for i in range(MAX_RETRIES):
            try:
                message = [{"role": "user", "content": prompt}]
 
                response = query_openai(
                    model=model_name,
                    messages=message,
                    temperature=0.1,
                    max_tokens=512,
                    simulation=simulation,  
                    print_cost=True  
                )
                return response["choices"][0]["message"]["content"]
            except Exception as e:
                errors += 1
                print(f"\nWARNING: Attempt {i + 1} failed due to error: {str(e)}")
                time.sleep(8.65)   
                if errors >= MAX_RETRIES:
                    print(
                        f"ERROR: Failed to get completion after {MAX_RETRIES} consecutive attempts for prompt: {prompt}")
                    raise


def get_answer_from_completion(prompt, model, hf_model=None, hf_tokenizer=None, start_index=0, simulation=False, current_output_directory=None,problem_index=None):
    completion_responses = []
    consecutive_errors_allowed = 3  # Circuit breaker threshold
    consecutive_errors = 0  # Current count of consecutive errors


    try:
        output_file_path = os.path.join(current_output_directory, f"{problem_index}.txt")

        if os.path.exists(output_file_path):
            return

        response = get_completion(prompt, model, hf_model, hf_tokenizer, simulation)
        completion_responses.append(response)

        print(f"\n=============== {problem_index} ================\n")
        print("\n------------ Prompt ------------\n")
        print(prompt)
        print("\n--------- Model Response --------\n")
        print(response)
        print("\n==================================\n")
        
        
        #time.sleep(0.5)  # Sleep for 0.5 seconds to avoid rate limiting

        formatted_content = f"Prompt: {prompt.strip()}\n\nResponse: {response.strip()}\n\n\n"

        if simulation is False:
            save(formatted_content, output_file_path)

        # save the response to a file
        #save(formatted_content, output_file_path)

        consecutive_errors = 0  # Reset the error count after a successful request
        
        # break

    except Exception as e:
        print(f"Failed to process prompt {problem_index}: {str(e)}")
        consecutive_errors += 1
        if consecutive_errors >= consecutive_errors_allowed:
            print("Circuit breaker triggered. Stopping the process.")
            return

    return completion_responses


def get_and_sotre_incorrect_problems(model_output_summary,output_directory_path,model):
     
    # store incorrect problems for each model at each level
    incorrect_problems = {}


    for level in model_output_summary[3]:
        incorrect_problems[level] = {}
        for problem_index, problem in model_output_summary[3][level].items():
            # store the incorrect problems for each model at each level
            if level == "Originals":
                if not problem["is_correct"]:
                    incorrect_problems[level][problem_index] = problem
            else:
                incorrect_problems[level][problem_index] = {}
                for variant_index, variant in problem.items():
                    if not variant["is_correct"]:
                        incorrect_problems[level][problem_index][variant_index] = variant

    model_name = model.split("/")[-1]

    thread_models_path = f"{output_directory_path}/incorrect_problems"
    if not os.path.exists(thread_models_path):
        os.makedirs(thread_models_path)

    save(json.dumps(incorrect_problems,indent=4), f"{thread_models_path}/{model_name}.json")

    print(f"Saved incorrect problems at {thread_models_path}/{model_name}.json\n")

    return incorrect_problems


def extract_problem_solutions(filename, levels):
    with open(filename) as f:
        questions = json.load(f)

    # sort the questions by index
    questions =  {k: v for k, v in sorted(questions.items(), key=lambda item: int(item[0]))}

    # rename the keys to 0,1,2,3,4,5,6,7,8,9
    #questions = dict(zip(range(len(questions)), questions.values()))
 
    result = defaultdict(dict)
    for level in levels:
        result[level] = {}

    for problem_index, problem in questions.items():
        for level in levels:
            result[level][problem_index] = problem[level]

    return result


def read_all_json_in_directory(directory_path):
    master_data = {}

    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            with open(os.path.join(directory_path, filename), 'r') as file:
                data = json.load(file)
                master_data[filename.split(".json")[0]] = data
    return master_data