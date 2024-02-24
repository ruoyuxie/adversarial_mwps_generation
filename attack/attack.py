# from transformers import AutoModelForCausalLM, AutoTokenizer
# from torch import cuda
# import torch
import argparse
from collections import defaultdict
import json
import gc
import os
from eval import eval_model, calculate_accuracy
from universal_attack import find_universal_attacks
from utils import get_answer_from_completion, generate_prompt, get_and_sotre_incorrect_problems, save,api_key_setup, extract_problem_solutions,read_all_json_in_directory
from experiment import human_eval_data_gen, universal_attack_pair_wise, num_of_adversarial_examples, debug


def load_hf_model_and_tokenizer(model_name):

    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
    print(f"Number of GPUs: {cuda.device_count()}")

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map='auto',
    )

    print(f"Model loaded on {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token_id = 0 if tokenizer.pad_token_id is None else tokenizer.pad_token_id
    print(f"Tokenizer loaded on {device}")

    return model, tokenizer



def process_problem_number(input_file, output_directory, model,  hf_model=None, hf_tokenizer=None, simulation=False,levels=None):

    data = extract_problem_solutions(input_file,levels)

    for level in levels:

        print(f"\n-- Processing [{level}] questions --\n")
              
        current_output_directory = os.path.join(output_directory, level)
        if not os.path.exists(current_output_directory):
            os.makedirs(current_output_directory)

        current_problems = data[level]
        all_responses = {}

        if level == "Originals":
            
            all_responses[level] = {}
            for problem_index, problem in enumerate(current_problems.items()):
                prompt = generate_prompt(problem[1][0])
                response = get_answer_from_completion(prompt, model, hf_model=hf_model, hf_tokenizer=hf_tokenizer, simulation=simulation, current_output_directory=current_output_directory, problem_index=int(problem[0]))
                all_responses[level][problem_index] = response

                
        else:
            all_responses[level] = {}
            for prob_index, probs in current_problems.items():
                if len(all_responses[level]) > 50:
                    break
                all_responses[level][prob_index] = {}
                problem_subfolder = os.path.join(current_output_directory, f"problem_{prob_index}")

                if not os.path.exists(problem_subfolder):
                    os.makedirs(problem_subfolder)

                print(f"\n-- Processing problem [{prob_index}] --\n")
                for index, variant in enumerate(probs):
                    prompt = generate_prompt(variant[0])
                        
                    response = get_answer_from_completion(prompt, model, hf_model=hf_model, hf_tokenizer=hf_tokenizer,  simulation=simulation, current_output_directory=problem_subfolder, problem_index=index)
                    all_responses[level][prob_index][index] = response

                # if simulation:
                #     os.rmdir(problem_subfolder)

def run_model(model, json_filepath=None, simulation=False,main_output_directory_path=None,levels=None):

    print(f"\n\n==================== {model} Inference Started ====================\n\n")

    hf_model, hf_tokenizer = None, None

    if "gpt" not in model:
        hf_model, hf_tokenizer = load_hf_model_and_tokenizer(model)

    model = model.split("/")[-1]

    api_key_setup(model)

    data_file_name = json_filepath.split("/")[-1].split(".")[0]

    if json_filepath:
        output_directory = os.path.join(main_output_directory_path, data_file_name, model)

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        process_problem_number(json_filepath, output_directory, model, hf_model=hf_model, hf_tokenizer=hf_tokenizer, simulation=simulation,levels=levels)

    print(f"\n\n==================== {model} Inference Completed ====================\n\n")

    try:
        del hf_model
        del hf_tokenizer
        del model
        gc.collect()
        cuda.empty_cache() 
    except:
        pass


def main(adversarial_data_path=None, model=None, simulation=False, main_output_directory_path=None, method=3):
    
    model_list = ["gpt-3.5-turbo-1106"]

    if model:
        model_list = [model]
    elif model is list:
        model_list = model
   

    if method == 1:
        levels = ["Originals", "M1"]
    elif method == 2:
        levels = ["Originals", "M2"]
    elif method == 3:
        levels = ["Originals", "M3"]
    

    data_path=adversarial_data_path

    simulation = False # debug: set to True to run in simulation mode without calling the openai API

    model_output_summary_path = os.path.join(main_output_directory_path, "model_output_summary")
       
    if not os.path.exists(model_output_summary_path):
        os.makedirs(model_output_summary_path)

    all_incorrect_problems = defaultdict(list)
    model_output_summary = {}

    for model in model_list:
        model_name = model.split("/")[-1]

        run_model(model, json_filepath=data_path, simulation=simulation,main_output_directory_path=main_output_directory_path,levels=levels)

        model_output_summary[model_name] = eval_model(model=model, json_filepath=data_path,main_result_path=main_output_directory_path,levels=levels)

        save(json.dumps(model_output_summary[model_name],indent=4), f"{model_output_summary_path}/{model_name}.json")
        print(f"\nSaved model output summary at {model_output_summary_path}/{model_name}.json")

        model_output_summary[model_name] = json.load(open(f"{model_output_summary_path}/{model_name}.json"))

        incorrect_problems = get_and_sotre_incorrect_problems (model_output_summary[model_name],main_output_directory_path,model)

        all_incorrect_problems[model_name] = incorrect_problems


    # debug(model_list, levels, model_output_summary_path)

    # # number of adversarial example experiement
    # num_of_adversarial_examples(levels, model_output_summary)

    # # universal attack pair-wise
    # universal_attack_pair_wise(main_output_directory_path, levels, all_incorrect_problems, model_output_summary)

    # # Create new incorrect problems for HUMAN EVALUATION
    # human_eval_data_gen(levels, all_incorrect_problems, model_output_summary)

    # #Find overlap between all models
    # find_universal_attacks(model_output_summary,main_output_directory_path,all_incorrect_problems,levels)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--model', help='"mistralai/Mistral-7B-v0.1", "meta-math/MetaMath-7B-V1.0", "WizardLM/WizardMath-13B-V1.0", "lmsys/vicuna-13b-v1.5", "meta-llama/Llama-2-13b-hf", "codellama/CodeLlama-34b-hf", "meta-llama/Llama-2-70b-hf", "meta-math/MetaMath-70B-V1.0", "gpt-3.5-turbo-1106", "gpt-4-0125-preview"', required=False)
    parser.add_argument('--adversarial_data_path', help='adversarial examples path')
    parser.add_argument('--simulation', help='simulation: True or False', default=False, required=False)
    parser.add_argument('--main_output_directory_path', help='main_output_directory_path', required=False)
    args = parser.parse_args()
    parser.add_argument('--method', default=3, help='generation method', required=False)
    
    main(adversarial_data_path=args.adversarial_data_path, model=args.model, simulation=args.simulation, main_output_directory_path=args.main_output_directory_path, method=args.method)
