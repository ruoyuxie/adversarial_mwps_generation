import ast
import json
from code_visitor import ProbSolveTreeVisitor
from problem_solving_tree import *
import util
import config


class TreeLoader(object):
    def __init__(self, randoms):
        self.dict = {}

        with open(config.original_question_file) as f:
            orig_json = json.load(f)

        indices = []
        for i, (index, questions) in enumerate(randoms.items()):
            indices.append((int(questions['orig_index']), index))

        code_directory = config.code_directory
        for i, index in indices:
            json_file = orig_json

            code_file = code_directory + f'{i}.py'
            orig_question = json_file[i]['question']
            answer = util.to_num(json_file[i]['final_ans'])

            with open(code_file) as f:
                code = f.read()

            tree = ast.parse(code)
            visitor = ProbSolveTreeVisitor(orig_question, answer)
            visitor.visit(tree)

            self.dict[str(index)] = visitor

    def __getitem__(self, item):
        return self.dict[item]

    def __setitem__(self, key, value):
        self.dict[key] = value


def wrong_answers():
    res = {}
    orig_wrong = 0
    mod_wrong = 0

    with open(config.model_incorrect_file) as f:
        data: dict = json.load(f)

    for level, questions in data.items():
        if level == 'Originals':
            for index, question in questions.items():
                if not question['is_correct']:
                    res[(index, -1, None)] = True
                    orig_wrong += 1
        else:
            for index, question_subsets in questions.items():
                for variant_index, question in question_subsets.items():
                    if not question['is_correct']:
                        res[(index, variant_index, level)] = True
                        mod_wrong += 1

    return res


def obtain_all_features(randoms):
    tree_loader = TreeLoader(randoms)
    features = set()
    for index, questions in randoms.items():
        for level, question_subset in questions.items():
            visitor = tree_loader[index]
            if level == "M3":
                for variant_index, (question, answer) in enumerate(question_subset):
                    problem_nums, formatted_problem = util.get_all_num_from_string(question)
                    for changed_value, node in zip(problem_nums, visitor.assign_node):
                        if node is not None:
                            node: VarNode = node
                            node.set_val(changed_value)
                    feature_map = FeatureMap()
                    visitor.get_answer_node().obtain_features(feature_map, prefix='final')
                    for feature in feature_map.feature_map.keys():
                        features.add(feature)

    features = list(features)
    features.sort()
    features_str = "\n".join(features)
    with open(config.analysis_output_dir + "features.txt", 'w') as f:
        f.write(features_str)


def process_features():
    def add_features(question, index, variant_index, level):
        problem_nums, formatted_problem = util.get_all_num_from_string(question)
        for changed_value, node in zip(problem_nums, visitor.assign_node):
            if node is not None:
                node: VarNode = node
                node.set_val(changed_value)
        new_id = feature_map.obtain_id(question)
        visitor.get_answer_node().obtain_features(feature_map, prefix='final')
        level = "Original" if level is None else level
        # feature_map.add_feature(level, 1)
        x = feature_map.create_feature_vector()
        y = (index, variant_index, level) not in wrong_ans.keys()
        if y:
            nums[0] += 1
        else:
            nums[1] += 1
        data_set.append((x, y))
        feature_map.add_to_feature_id_map(new_id, x, y)

    with open(config.random_file_name) as f:
        randoms: dict = json.load(f)

    obtain_all_features(randoms)
    FeatureMap.reinit()
    feature_map = FeatureMap(add_new=False)
    wrong_ans = wrong_answers()
    tree_loader = TreeLoader(randoms)
    data_set = []
    nums = [0, 0]
    for index, questions in randoms.items():
        for level, question_subset in questions.items():
            visitor = tree_loader[index]
            if level == "M3":
                for variant_index, (question, answer) in enumerate(question_subset):
                    variant_index = str(variant_index)
                    add_features(question, index, variant_index, level)

    with open(config.analysis_output_dir + "feature_vectors.txt", 'w') as f:
        json.dump(data_set, f)
    with open(config.analysis_output_dir + 'feature_ids.json', 'w') as f:
        json.dump(feature_map.feature_id_map, f, indent=2)
    with open(config.analysis_output_dir + 'id_to_question.json', 'w') as f:
        json.dump(feature_map.id_question_map, f, indent=2)

    # Calculate correct rate of features
    correct_count = nums[0]
    total_ques_count = sum(nums)

    feature_correct_rate = ""
    feature_per_val_correct_rate = {}
    for feature in FeatureMap.default_keys:
        feature_list = feature_map.feature_id_map[feature]
        feature_len = len(feature_list)
        correct_num = 0
        for (ques_id, feature_val, correct) in feature_list:
            correct_num += 1 if correct else 0
        correct_rate = round(correct_num / feature_len, 2)
        feature_correct_rate += f'{feature}: {feature_len}, {correct_rate}\n'

        cur_correct_count = correct_count
        cur_total_count = total_ques_count - feature_len
        feature_id_correctness_dict = dict()
        correct_num = 0
        for (ques_id, feature_val, correct) in feature_list:
            if feature_val in feature_id_correctness_dict:
                feature_correct_count, feature_total_count = feature_id_correctness_dict[feature_val]
                feature_correct_count += 1 if correct else 0
                feature_total_count += 1
                feature_id_correctness_dict[feature_val] = (feature_correct_count, feature_total_count)
            else:
                feature_id_correctness_dict[feature_val] = (1 if correct else 0, 1)
            correct_num += 1 if correct else 0
        cur_correct_count -= correct_num
        feature_id_correctness_dict[0] = (cur_correct_count, cur_total_count)
        feature_per_val_correct_rate[feature] = feature_id_correctness_dict

    with open(config.analysis_output_dir + 'selected_features.json', 'a+') as f:
        try:
            all_model_dict = json.load(f)
        except json.decoder.JSONDecodeError:
            all_model_dict = {}

    output_dict = {}
    for k, v in feature_per_val_correct_rate.items():
        key_list = list(v.keys())
        key_list.sort()
        if k in ["operation_count", "Mult_count"]:
            total_rate_list = {}
            for val in key_list:
                cor_count = v[val][0]
                total_count = v[val][1]
                if total_count == 0:
                    continue
                else:
                    rate = round(cor_count / total_count, 3)
                    total_rate_list[val] = [total_count, rate]
            output_dict[k] = total_rate_list
        elif "final_log" in k or "end_log" in k:
            prefix = k.split('_')[0]
            range_val = int(k.split('_')[-1])

            lower_range = util.to_int_if_int(math.pow(2.0, 2 * range_val - 1))
            upper_range = util.to_int_if_int(math.pow(2.0, 2 * range_val + 1))
            sub_key = f'[{lower_range}, {upper_range})'

            key = "Answer Range" if prefix == 'final' else "Generated Range"
            total_rate_list = {} if key not in output_dict else output_dict[key]

            cor_count = 0
            total_count = 0
            for val in key_list:
                if val == "0":
                    continue
                cor_count += v[val][0] * int(val)
                total_count += v[val][1] * int(val)

            rate = round(cor_count / total_count, 3)
            total_rate_list[sub_key] = [total_count, rate]
            output_dict[key] = total_rate_list

    all_model_dict[config.model_name] = output_dict
    with open(config.analysis_output_dir + 'selected_features.json', 'w') as f:
        json.dump(all_model_dict, f, indent=2)
