import os
import json
from clean_output import convert_string_to_float, extract_numerical_value
from utils import extract_problem_solutions


def extract_model_output_and_compare(problem, model_output_file, gold_answer, original_problem_index, all_comparsion_results, level,variant_index=None):
    if os.path.exists(model_output_file):
        try:
            with open(model_output_file, 'r') as file:
                model_output = file.read().strip()

                
                extracted_value = extract_numerical_value(model_output)
                extracted_value = convert_string_to_float(extracted_value) if extracted_value else None

                gold_answer = round(gold_answer, 2)

                if level == "Originals":
                    all_comparsion_results[level][original_problem_index] = {
                        "problem_index": int(original_problem_index),
                        "problem": problem,
                        "gold_answer": gold_answer,
                        "model_output": model_output,
                        "extracted_value": extracted_value,
                        "is_correct": extracted_value == gold_answer
                    }
                else:
                    all_comparsion_results[level][original_problem_index][variant_index] = {
                        "problem_index": int(original_problem_index),
                        "variant_index": variant_index,
                        "problem": problem,
                        "gold_answer": gold_answer,
                        "model_output": model_output,
                        "extracted_value": extracted_value,
                        "is_correct": extracted_value == gold_answer
                    }

        except:
            print("\n============ Extraction Error ===============\n")
                # print(f"Error in subfolder {os.path.basename(os.path.dirname(json_path))}, problem {problem_index}")
                # print(f"Model output: {model_output}")
                # print(f"Extracted value: {extracted_value}")
                # print(f"Gold answer: {gold_answer}")
                # print("\n=============================================\n")
            pass



def compare_model_outputs(json_path, output_folder_path,levels):

    data = extract_problem_solutions(json_path,levels)

    all_comparsion_results = {}

    for level in levels:
        all_comparsion_results[level] = {}

        for _, problem in enumerate(data[level].items()):
            original_problem_index = problem[0]

            if level == "Originals":
                current_gold_answer = problem[1][1]
                current_problem = problem[1][0]
                model_output_file = os.path.join(output_folder_path, level, f"{original_problem_index}.txt")
                extract_model_output_and_compare(current_problem, model_output_file, current_gold_answer, original_problem_index, all_comparsion_results, level)
            else:
                for _ in enumerate(problem):
                    # if original_problem_index ==10:
                    #     print("here")
                    all_comparsion_results[level][original_problem_index] = {}
                    list_of_variants = problem[1]
                    for variant_index, proble in enumerate(list_of_variants):

                        current_gold_answer = proble[1]
                        current_variant = proble[0]
                        model_output_file = os.path.join(output_folder_path, level, f"problem_{original_problem_index}", f"{variant_index}.txt")
                        extract_model_output_and_compare(current_variant, model_output_file, current_gold_answer, original_problem_index, all_comparsion_results, level,variant_index=variant_index)

    return all_comparsion_results

def print_incorrect_problems(all_comparsion_results,levels,model_name=None):
    print(f"\n********** [{model_name}] Incorrect Problems **********")
    # print the details of the incorrect problems from all_comparsion_results
    for level in levels:
        print(f"\n********** {level} **********")
        for problem_index, problem in all_comparsion_results[level].items():
            if level == "Originals":
                if not problem["is_correct"]:
                    # json dump with indent=4 makes the output more readable
                    print(json.dumps(problem, indent=4))
            else:
                for variant_index, variant in problem.items():
                    if not variant["is_correct"]:
                        print(json.dumps(variant, indent=4))

        print("\n*****************************************\n")

print("\n")


def calculate_accuracy(all_comparsion_results,levels,debug=False ,model_name=None):

    print(f"\n********** [{model_name}] Results **********")

    all_results = {}
    for level in levels:
        all_results[level] = {}
        for problem_index, problem in all_comparsion_results[level].items():
            if level == "Originals":
                all_results[level][problem_index] = problem["is_correct"]
            else:
                all_results[level][problem_index] = {}
                for variant_index, variant in problem.items():
                    all_results[level][problem_index][variant_index] = variant["is_correct"]


    all_accuracy = {}
    for level in levels:
        all_accuracy[level] = {}
        for problem_index, problem in all_results[level].items():
            if level == "Originals":
                all_accuracy[level] = sum(1 for result in all_results[level].values() if result) / len(all_results[level]) * 100
            else:
                for variant_index, variant in problem.items():
                    all_accuracy[level][problem_index] = sum(1 for result in all_results[level][problem_index].values() if result) / len(all_results[level][problem_index]) * 100
                
    finalized_accuracy = {}
    for level in levels:
        if level == "Originals":
            finalized_accuracy[level] = round(all_accuracy[level], 2)
        else:
            # for other levels, if the problem does not have accuracy to 100%, it is considered as incorrect
            try:
                finalized_accuracy[level] = round(sum(1 for result in all_accuracy[level].values() if result == 100) / len(all_accuracy[level]) * 100, 2)
            except:
                finalized_accuracy[level] = 0.0

        
    for level in levels:
        # print number of total problems and number of incorrect problems
        if level == "Originals":
            print(f"\n********** {level} **********")
            print(f"Total problems: {len(all_results[level])}")
            print(f"Correct answers: {sum(1 for result in all_results[level].values() if result)}")
            print(f"Incorrect answers: {len(all_results[level]) - sum(1 for result in all_results[level].values() if result)}")
            print(f"Accuracy: {round(finalized_accuracy[level],2)}%")
        else:
            print(f"\n********** {level} **********")
            print(f"Total problems: {len(all_accuracy[level])}")
            print(f"Correct answers: {sum(1 for result in all_accuracy[level].values() if result == 100)}")
            print(f"Incorrect answers: {sum(1 for result in all_accuracy[level].values() if result != 100)}")
            print(f"Accuracy: {round(finalized_accuracy[level],2)}%")

    if debug:
        print_incorrect_problems(all_comparsion_results,levels,model_name)

    return finalized_accuracy,all_accuracy,all_results


def eval_model(model=None, json_filepath=None,main_result_path=None,levels=None):

    data_file_name = json_filepath.split("/")[-1].split(".")[0]
    
    debug = False
    
    model_name = model.split("/")[-1]

    if json_filepath:
        model_output_folder = os.path.join(main_result_path, data_file_name, model_name)
        if "attacked_from" in main_result_path or "verify_from" in main_result_path:
            model_output_folder = os.path.join(main_result_path, model_name)

        
        all_comparsion_results = compare_model_outputs(json_filepath, model_output_folder, levels)

        finalized_accuracy,all_accuracy,all_results = calculate_accuracy(all_comparsion_results,levels,debug,model_name)

        return finalized_accuracy,all_accuracy,all_results,all_comparsion_results

if __name__ == "__main__":
    eval_model()