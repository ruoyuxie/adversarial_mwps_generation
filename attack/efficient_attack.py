import os
import json
from utils import get_answer_from_completion, generate_prompt, api_key_setup
from eval import eval_model, compare_model_outputs, calculate_accuracy,extract_numerical_value,convert_string_to_float
import random
random.seed(42)


def attack(incorrect_problems, victim_model, simulation=False, main_output_directory_path=None, levels=None, thread_model=None, model_output_summary=None, verify=False):

    print(f"\n\n==================== Victim model: {victim_model} ====================\n\n")
    # previous folder of main_output_directory_path
    main_results_path =  os.path.dirname(main_output_directory_path)
    victim_model_output_directory_path = os.path.join(main_results_path,"victim_models", f"{victim_model}")
    if not os.path.exists(victim_model_output_directory_path):
        os.makedirs(victim_model_output_directory_path)

    if verify:
        victim_thread_model_output_directory_path = os.path.join(victim_model_output_directory_path, "verify_from", thread_model.split('/')[-1])
    else:
        victim_thread_model_output_directory_path = os.path.join(victim_model_output_directory_path, "attacked_from", thread_model.split('/')[-1])
    if not os.path.exists(victim_thread_model_output_directory_path):
        os.makedirs(victim_thread_model_output_directory_path)


    for level in levels:

        print(f"\n\n==================== Level: {level} ====================\n\n")

        victim_thread_model_level_output_directory_path = os.path.join(victim_thread_model_output_directory_path, level)
        if not os.path.exists(victim_thread_model_level_output_directory_path):
            os.makedirs(victim_thread_model_level_output_directory_path)

        current_problems = incorrect_problems[level]
        current_problems = dict(sorted(current_problems.items(), key=lambda item: len(item[1]), reverse=True))


        clean_current_modified_problems = {}


        # remove the empty directories from current_problems
        if level != "Originals":
            for prob_index, prob in current_problems.items():
                if len(prob) != 0 and len(clean_current_modified_problems) < 50:
                    clean_current_modified_problems[prob_index] = []
                    for variant_index, variant in prob.items():
                        # only store 50 variants for each problem
                        #if len(clean_current_modified_problems[prob_index]) < 50:
                        clean_current_modified_problems[prob_index].append(variant)
                    
        if verify: 
            # stored only the problem that is 100
            clean_current_modified_problems = {}

            for prob_index, probs in model_output_summary[1]["M3"].items():
                if probs == 100:
                    clean_current_modified_problems[prob_index] = []

                    for variant_index, variant in model_output_summary[3]["M3"][prob_index].items():
                        clean_current_modified_problems[prob_index].append(variant)

            # ramdomly select 5 problems
            clean_current_modified_problems = dict(random.sample(clean_current_modified_problems.items(), 5))

        # else:
        #     # rank clean_current_modified_problems based on the number of variants and only get the top 5
        #     clean_current_modified_problems = dict(sorted(clean_current_modified_problems.items(), key=lambda item: len(item[1]), reverse=True[:5])

        current_original_problems = model_output_summary[3]["Originals"]

        clean_current_original_problems = {}
        # only sotre the problem that is in clean_current_modified_problems
        for prob_index, prob in current_original_problems.items():
            if str(prob["problem_index"]) in clean_current_modified_problems:
                clean_current_original_problems[str(prob["problem_index"])] = prob
        

        # make api call 
        all_responses = {}

        if level == "Originals":
            all_responses[level] = {}
            for problem_index, problem in clean_current_original_problems.items():
                prompt = generate_prompt(problem["problem"])
                response = get_answer_from_completion(prompt, victim_model, hf_model=None, hf_tokenizer=None, start_index=0, simulation=simulation, current_output_directory=victim_thread_model_level_output_directory_path)
                all_responses[level][problem_index] = response   
        else:
            all_responses[level] = {} #M3
            for prob_index, probs in clean_current_modified_problems.items():
                # create a subfolder for each problem
                problem_subfolder = os.path.join(victim_thread_model_level_output_directory_path, f"problem_{prob_index}")
                all_responses[level][prob_index] = {}
                
                # if not os.path.exists(problem_subfolder) and simulation == False:
                #     os.makedirs(problem_subfolder)

                if not os.path.exists(problem_subfolder):
                    os.makedirs(problem_subfolder)


                print(f"\n-- Processing problem [{prob_index}] --\n")
                for variant in probs:
                    prompt = generate_prompt(variant["problem"])
                    variant_index = variant["variant_index"]
                    gold_answer = variant["gold_answer"]

                    response = get_answer_from_completion(prompt, victim_model, hf_model=None, hf_tokenizer=None, start_index=0, simulation=simulation, current_output_directory=problem_subfolder, problem_index=variant_index)

                    if not response:
                        continue

                    extracted_value = extract_numerical_value(response[0])
                    extracted_value = convert_string_to_float(extracted_value) if extracted_value else None

                    gold_answer = round(gold_answer, 2)


                    all_responses[level][prob_index][variant_index] = response
                    
                    if extracted_value:
                        if extracted_value != gold_answer:
                            print(f"\n\n======= Sueecssful Attack at variant [{variant_index}] =======")
                            print(f"Gold answer: {gold_answer}; Extracted value: {extracted_value}\n\n")
                            break

                #     break
                # break

    return all_responses, victim_thread_model_output_directory_path



def execute_attack(thread_models, victim_models,simulation=False,incorrect_problem_directory_path=None,levels=None,model_output_summary_path=None,json_filepath=None,verify=False):
 
    print(f"\n\n==================== Efficient Attack Started ====================\n\n")

    print(f"\n\n==================== Verification: {verify} ====================\n\n")

    for thread_model in thread_models:
        # read the incorrect problems for each model at each level
        incorrect_problems = json.load(open(f"{incorrect_problem_directory_path}/{thread_model.split('/')[-1]}.json"))



        model_output_summary = json.load(open(f"{model_output_summary_path}/{thread_model.split('/')[-1]}.json"))

        print(f"\n\n==================== Thread model: {thread_model} ====================\n\n")

        for victim_model in victim_models:
            if verify:
                victim_model_output_directory_path = os.path.join(os.path.dirname(incorrect_problem_directory_path),"victim_models", f"{victim_model}", "verify_from")
            else:
                victim_model_output_directory_path = os.path.join(os.path.dirname(incorrect_problem_directory_path),"victim_models", f"{victim_model}", "attacked_from")

            api_key_setup(victim_model)
            attack (incorrect_problems, victim_model, simulation=simulation, main_output_directory_path=incorrect_problem_directory_path, levels=levels, thread_model=thread_model, model_output_summary=model_output_summary,verify=verify)

            eval_model(model=thread_model, json_filepath=json_filepath,main_result_path=victim_model_output_directory_path,levels=levels)

        # break


def efficient_attack ():

    simulation = False
    
    verify = False

    incorrect_problem_directory_path = f"/usr/project/xtmp/rx55/projects/aallm/main_results/incorrect_problems/"
    model_output_summary_path = f"/usr/project/xtmp/rx55/projects/aallm/main_results/model_output_summary/"
    json_filepath = f"/usr/project/xtmp/rx55/projects/aallm/generated/adversarial_example.json"

    levels = [
           # "Originals", 
            "M3", 
           # "M2",
           # "M1"
        ]


    thread_models = ["gpt-3.5-turbo-1106","meta-math/MetaMath-70B-V1.0","meta-math/MetaMath-7B-V1.0", "WizardLM/WizardMath-13B-V1.0"]

    #thread_models = ["meta-math/MetaMath-70B-V1.0"]

    victim_models = ["gpt-4-0125-preview"]

    execute_attack(thread_models,victim_models, simulation=simulation,incorrect_problem_directory_path=incorrect_problem_directory_path, levels=levels,model_output_summary_path=model_output_summary_path,json_filepath=json_filepath,verify=verify)

if __name__ == "__main__":
    efficient_attack()
