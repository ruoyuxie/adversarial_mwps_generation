from utils import save
import json
import os

def find_universal_attacks(model_output_summary,output_directory_path,incorrect_problems,levels):

    # get incorrect problems for each model at each level
 
    # Dictionary to store the common overlap in incorrect problems among all models at each level
    universal_attacks = {}
    
    for model, data in incorrect_problems.items():
        for level in data:
            if level not in universal_attacks:
                universal_attacks[level] = {}
            for problem_index, problem in data[level].items():
                if level == "Originals":
                    if problem_index not in universal_attacks[level]:
                        universal_attacks[level][problem_index] = []
                    if model not in universal_attacks[level][problem_index]:
                        universal_attacks[level][problem_index].append(model)
                else:
                    if problem_index not in universal_attacks[level]:
                        universal_attacks[level][problem_index] = {}
                    for variant_index, variant in problem.items():
                        if variant_index not in universal_attacks[level][problem_index]:
                            universal_attacks[level][problem_index][variant_index] = []
                        if model not in universal_attacks[level][problem_index][variant_index]:
                            universal_attacks[level][problem_index][variant_index].append(model)

    print("\n\n==================== Universal Attacks ====================\n\n")

    print(f"\nModels: {list(model_output_summary.keys())}\n")
    print(f"Total Number of Problems: {len(model_output_summary[model][3][level])} ")


    common_overlap_details = {}


    for level, problem_per_model in universal_attacks.items():
        common_overlap_details[level] = {}
        for problem_index, problem in problem_per_model.items():
            if level == "Originals":
                if len(problem) == len(model_output_summary):
                    common_overlap_details[level][problem_index] = problem
                    # print(f"Problem {problem_index} is a universal attack")
            else:
                for variant_index, variant in problem.items():
                    if len(variant) == len(model_output_summary):
                        if problem_index not in common_overlap_details[level]:
                            common_overlap_details[level][problem_index] = {}
                        common_overlap_details[level][problem_index][variant_index] = variant
                        # print(f"Problem {problem_index} variant {variant_index} is a universal attack")


    for level, problem_per_model in common_overlap_details.items():
        if level not in levels:
            continue
        print(f"\n\n ==================== Level: {level} ====================\n\n")
        if level == "Originals":
            print(f"Universal attacks: {[int(key) for key in problem_per_model.keys()]} ")
            print(f"Number of Universal Attacks: {len(problem_per_model)}")
            print(f"Percentage of Universal Attacks: {len(problem_per_model)/len(model_output_summary[model][3][level])*100:.2f}%")
        else:
            
            # average_universal_attacks_per_problem = sum([len(problem) for problem in problem_per_model.values()])/len(problem_per_model)

            for problem_index, problem in problem_per_model.items():
                # print the universal attacks details for each problem, if needed
                #print(f"Problem [{problem_index}] has [{len(problem)}] universal attacks")
                #print(f"Universal Attacks: {[int(key) for key in problem.keys()]}\n")
                pass

            print(f"Number of Universal Attacks: {len(problem_per_model)}")
            print(f"Percentage of Universal Attacks: {len(problem_per_model)/len(incorrect_problems[model][level])*100:.2f}%\n")
            
    # map the universal attacks to the original problems from model_output_summary[model][3]， 
    universal_attack_map = {}
    for level, problem_per_model in common_overlap_details.items():
        universal_attack_map[level] = {}
        for problem_index, problem in problem_per_model.items():
            if level == "Originals":
                item = model_output_summary[model][3][level][problem_index]
                # only save the "problem" and "gold_answers" fields
                problem_answer = {key: item[key] for key in ["problem", "gold_answer"]}

                universal_attack_map[level][problem_index] = problem_answer
            else:
                universal_attack_map[level][problem_index] = {}
                for variant_index, variant in problem.items():
                    item = model_output_summary[model][3][level][problem_index][variant_index]
                    # only save the "problem" and "gold_answers" fields
                    problem_answer = {key: item[key] for key in ["problem", "gold_answer"]}
                    universal_attack_map[level][problem_index][variant_index] = problem_answer

    # save the universal attacks
    universal_attack_file_path = f"{output_directory_path}/universal_attacks"
    if not os.path.exists(universal_attack_file_path):
        os.makedirs(universal_attack_file_path)

    save(json.dumps(universal_attack_map,indent=4), f"{universal_attack_file_path}/universal.json")
    print(f"\nSaved universal attacks at {universal_attack_file_path}/universal.json\n")