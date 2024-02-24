
from utils import read_all_json_in_directory, save
from universal_attack import find_universal_attacks
from eval import calculate_accuracy
import json

def debug(model_list, levels, model_output_summary):
    model_output_summary = read_all_json_in_directory(model_output_summary)

    all_incorrect_problems = read_all_json_in_directory(f"/usr/project/xtmp/rx55/projects/aallm/main_results/incorrect_problems")
   
    for model in model_list:  # print accuracy for all models
        model_name = model.split("/")[-1]
        calculate_accuracy(model_output_summary[model_name][3], levels, debug=False, model_name=model_name)
    return model, all_incorrect_problems, model_output_summary

def human_eval_data_gen(levels, all_incorrect_problems, model_output_summary):
    model_list = ["gpt-3.5-turbo-1106"]
    import random
    random.seed(42)
    new_incorrect_problems = {}
    # fuliter out the incorrect problems 
    for model in model_list:
        model_name = model.split("/")[-1]
        for level in levels:
            # print(f"\n\n==================== {model_name} {level} ====================\n\n")
            if level != "Originals":
                new_incorrect_problems[level] = {}
                # randomly select 10 problems and select randomly 1 variant from each problem
                while len(new_incorrect_problems[level]) < 10:
                    random_problem = random.choice(list(all_incorrect_problems[model_name][level].keys()))
                    if model_output_summary[model_name][3]["Originals"][random_problem]["is_correct"] is False:
                        continue
                    if random_problem not in new_incorrect_problems[level] and len(all_incorrect_problems[model_name][level][random_problem]) > 1:
                        new_incorrect_problems[level][random_problem] = {}

                        while len(new_incorrect_problems[level][random_problem]) < 1:
                            random_variant = random.choice(list(all_incorrect_problems[model_name][level][random_problem].keys()))
                            if random_variant not in new_incorrect_problems[level][random_problem]:
                                new_incorrect_problems[level][random_problem][random_variant] = all_incorrect_problems[model_name][level][random_problem][random_variant]
                                original_probelm = model_output_summary[model_name][3]["Originals"][random_problem]
                                # add original_probelm as a field to the new_incorrect_problems
                                new_incorrect_problems[level][random_problem][random_variant].update({"original_problem": original_probelm})

                                original_probelm = model_output_summary[model_name][3]["Originals"][random_problem]["problem"]
                                original_answer = model_output_summary[model_name][3]["Originals"][random_problem]["gold_answer"]
                                modified_problem = new_incorrect_problems[level][random_problem][random_variant]["problem"]
                                modified_answer = new_incorrect_problems[level][random_problem][random_variant]["gold_answer"]
                                #print(f"Problem: {original_probelm} #### Answer: {original_answer}")
                                print(f"Modification: {modified_problem} #### Answer: {modified_answer}")
                    
    # save the new incorrect problems for human evaluation
    save(json.dumps(new_incorrect_problems, indent=4), f"/usr/project/xtmp/rx55/projects/aallm/main_results/human_evaluation/{model_name}.json")
    return model

def universal_attack_pair_wise(main_output_directory_path, levels, all_incorrect_problems, model_output_summary):
    model_list = ["mistralai/Mistral-7B-v0.1", "meta-math/MetaMath-7B-V1.0", "WizardLM/WizardMath-13B-V1.0", "lmsys/vicuna-13b-v1.5", "meta-llama/Llama-2-13b-hf", "codellama/CodeLlama-34b-hf", "meta-math/MetaMath-70B-V1.0","gpt-3.5-turbo-1106"]

    for model in model_list:
        model_name = model.split("/")[-1]
        # pair-wise comparison to find overlap between models
        for model2 in model_list:
            new_model_output_summary = {}
            new_incorrect_problems = {}
            # the new one only contains the two models
            new_model_output_summary[model_name] = model_output_summary[model_name]
            new_incorrect_problems[model_name] = all_incorrect_problems[model_name]
            if model != model2:
                model2_name = model2.split("/")[-1]
                new_model_output_summary[model2_name] = model_output_summary[model2_name]
                new_incorrect_problems[model2_name] = all_incorrect_problems[model2_name]
                print(f"\n\n==================== Overlap between {model_name} and {model2_name} ====================\n\n")
                find_universal_attacks(new_model_output_summary, main_output_directory_path, new_incorrect_problems, levels)

    # universal attack increase number of models
    model_list = ["mistralai/Mistral-7B-v0.1", "meta-math/MetaMath-7B-V1.0", "meta-llama/Llama-2-13b-hf", "WizardLM/WizardMath-13B-V1.0", "lmsys/vicuna-13b-v1.5", "meta-math/MetaMath-70B-V1.0","gpt-3.5-turbo-1106", "codellama/CodeLlama-34b-hf"]
    for model in model_list:
        model_name = model.split("/")[-1]
        # gradually increase the number of models to find overlap between models
        new_model_output_summary = {}
        new_incorrect_problems = {}
        for model2 in model_list:
            new_model_output_summary[model_name] = model_output_summary[model_name]
            new_incorrect_problems[model_name] = all_incorrect_problems[model_name]
            if model != model2:
                model2_name = model2.split("/")[-1]
                new_model_output_summary[model2_name] = model_output_summary[model2_name]
                new_incorrect_problems[model2_name] = all_incorrect_problems[model2_name]
                print(f"\n\n==================== Overlap between {len(new_model_output_summary)} models ====================\n\n")
                find_universal_attacks(new_model_output_summary, main_output_directory_path, new_incorrect_problems, levels)

def num_of_adversarial_examples(levels, model_output_summary):
    model_list = ["mistralai/Mistral-7B-v0.1", "meta-math/MetaMath-7B-V1.0", "WizardLM/WizardMath-13B-V1.0", "lmsys/vicuna-13b-v1.5", "meta-llama/Llama-2-13b-hf", "codellama/CodeLlama-34b-hf", "meta-math/MetaMath-70B-V1.0","gpt-3.5-turbo-1106"]
    number_of_variants = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    for variant_num in number_of_variants:
        print(f"\n\n==================== Variant Number: {variant_num} ====================\n\n")
        for model in model_list:  # print accuracy for all models
            model_name = model.split("/")[-1]
            current_model_data = model_output_summary[model_name][3]
            # for M3, M2, M1 in current_model_data,
            for level in current_model_data:
                if level != "Originals":
                    for problem_index, problem in current_model_data[level].items():
                            new_problem = {}
                            for variant_index, variant in problem.items():
                                # only keep variant_num number of variants
                                if int(variant_index) < variant_num:
                                    new_problem[variant_index] = variant
                            current_model_data[level][problem_index] = new_problem
        for model in model_list:  # print accuracy for all models
            model_name = model.split("/")[-1]
            calculate_accuracy(model_output_summary[model_name][3], levels, debug=False, model_name=model_name)
