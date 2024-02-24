import ast
import itertools
import json
import math
import random

import util
import config
from code_visitor import ProbSolveTreeVisitor, NumberCounter
from gpt_code_prompt import ask_gpt
from tqdm import tqdm


def generate_instances_of_questions(original_question_file, output_file_name, code_directory, ignore_index=None, counts=30_000, seed=42,level=3):

    print("Generating adversarial examples...")

    code_file_format = "{}.py"
    random.seed(seed)

    def code_file_name(i):
        return (code_directory + code_file_format).format(i)

    def get_questions_json():
        with open(original_question_file) as _f:
            _original_json = json.load(_f)

        _codes = []
        for _i in range(len(_original_json)):
            with open(code_file_name(_i)) as _f:
                _codes.append(_f.read())

        assert len(_original_json) == len(_codes), "Code and questions have different length"

        return _original_json, _codes

    original_json, codes = get_questions_json()
    generated_question_list = []
    error_list = {
        "Has Loop": [],
        "Wrong Answer": [],
        "Number Misalignment": [],
        "Has Comparison": [],
    }

    for i in range(len(original_json)):
        if ignore_index is not None and i in ignore_index:
            continue

        print(f'Question #{i}')

        code = codes[i]
        tree = ast.parse(code)
        original_question = original_json[i]['question']
        answer = util.to_num(original_json[i]['final_ans'])

        # Extract all numbers from the original question
        ques_numbers, formatted_question = util.get_all_num_from_string(original_question)

        # Checking Number Misalignment
        visitor = NumberCounter()
        visitor.visit(tree)
        code_numbers = visitor.numbers

        # Check the scenarios
        ques_num_set = set(ques_numbers)
        skip_question = False
        version_count = 1
        for num in ques_num_set:
            ques_count = ques_numbers.count(num)
            code_count = code_numbers.count(num)

            # Doesn't appear in code, is constant in the question
            if code_count == 0:
                continue
            # Number misalignment
            if ques_count < code_count or ques_count > code_count:
                skip_question = True
                break
            version_count *= math.factorial(ques_count)
        if skip_question:
            error_list['Number Misalignment'].append(i)
            continue

        # Use visitor to get the structure of the code
        try:
            visitor = ProbSolveTreeVisitor(original_question, answer)
            visitor.visit(tree)
            visitor.generate_versions()
            visitor.merge_versions()

            if config.distinguish_using_gpt:
                distinguishing, answers = visitor.produce_distinguishing_question()
                answer_from_gpt = ask_gpt(distinguishing)
                index = util.get_index_in_list(answer_from_gpt, answers)
                if index > -1:
                    visitor.versions = [visitor.versions[index]]
                else:
                    error_list['Number Misalignment'].append(i)
                    continue
            else:
                # If not using GPT to distinguish, then we will just choose the first one.
                visitor.versions = visitor.versions[:1]

        except NotImplementedError as e:
            if str(e) == "Has while" or str(e) == "Has for" or str(e) == "Has if":
                error_list['Has Loop'].append(i)
                continue
            if str(e) == "Wrong answer":
                error_list['Wrong Answer'].append(i)
                continue
            if str(e) == "Node Operation Compare":
                error_list['Has Comparison'].append(i)
                continue
            raise e

        # Generate new question instances
        nums_answer_pairs = {tuple(ques_numbers): True}
        nums_answer_dict = {}
        for requirement in itertools.product([True, False], repeat=6):
            requirement = list(requirement)
            nums_answer_dict[str(requirement)] = []

        if level == 3:
            requirements = ['M3']
        if level == 2:
            requirements = ['M2']
        if level == 1:
            requirements = ['M1']

        for req in requirements:
            # print(f"Generating {req}: ")
            for _ in tqdm(range(counts)):
                try:
                    new_nums, reqs = visitor.get_new_instance(req)
                    new_answer = visitor.get_answer()
                except ZeroDivisionError:
                    continue
                if tuple(new_nums) not in nums_answer_pairs:
                    nums_answer_pairs[tuple(new_nums)] = True
                    nums_answer_dict[str(reqs)].append([new_nums, new_answer])

        # Construct the question json
        original_answer = util.to_num(original_json[i]['final_ans'])
        question_dict = {
            'formatted_question': formatted_question,
            'generated_instances': nums_answer_dict,
            'original_pair': [ques_numbers, original_answer],
            'index': i
        }

        # Add to resulting list
        generated_question_list.append(question_dict)

    # Display questions errors for debugging
    # for key, value in error_list.items():
    #     print(f'{key}: {len(value)}, {value}')

    # Write to file
    with open(output_file_name, 'w') as f:
        json.dump(generated_question_list, f, indent=2)


def post_process(original_file, output_file):
    def filter_req(req: str):
        req = req[1:-1]
        req = [x == 'True' for x in req.split(', ')]

        _req = [False, False, False]
        if req[0] and req[1] and req[5]:
            _req[0] = True
        if req[4] and req[2]:
            _req[2] = True
            _req[1] = True
        elif req[4]:
            _req[1] = True

        res = None
        if _req == [True, True, True]:
            res = "M3"
        elif _req == [True, True, False]:
            res = "M2"
        elif _req == [True, False, False]:
            res = "M1"

        return res

    with open(original_file) as f:
        questions = json.load(f)

    questions_new = {}

    for question in questions:
        i = question['index']
        formatted_question = question['formatted_question']
        questions_new[i] = {}
        questions_new[i]['formatted_question'] = formatted_question
        questions_new[i]['original_pair'] = question['original_pair']
        questions_new[i]['generated_instances'] = {}
        generated_new = questions_new[i]['generated_instances']
        for requirement, _questions in question['generated_instances'].items():
            new_req = filter_req(requirement)
            if not new_req:
                continue
            if new_req in generated_new.keys():
                generated_new[new_req] += _questions
            else:
                generated_new[new_req] = _questions
        questions_new[i]['stat'] = {}
        for requirement, _questions in generated_new.items():
            questions_new[i]['stat'][requirement] = len(generated_new[requirement])

    with open(output_file, 'w') as f:
        json.dump(questions_new, f, indent=2)


def choose_random_from_given_level(input_file, output_file, n=100, m=100, seed=42, level=3):
    random.seed(seed)

    with open(input_file) as f:
        questions: dict = json.load(f)

    randoms = {}
    answers = {}
    indices = list(questions.keys())
    random_indices = random.sample(indices, len(indices))
    counts = 0

    if level == 3:
        levels = ["Originals", "M3"]
    if level == 2:
        levels = ["Originals", "M2"]
    if level == 1:
        levels = ["Originals", "M1"]

    for level in levels:
        randoms[level] = []
        answers[level] = []

    new_questions = {}

    for i in random_indices:
        if counts == n:
            break

        question = questions[i]
        instances = question['generated_instances']

        has_enough_questions = True
        for level in levels[1:]:
            if len(instances[level]) < m:
                has_enough_questions = False
                break
            nums, answer = instances[level][0]
            for num in nums:
                if num is None:
                    has_enough_questions = False

        if not has_enough_questions:
            print(f"Skipping question {i} because it doesn't have enough valid modifications.")
            continue

        new_questions[counts] = {"orig_index": i}
        for level in levels:
            new_questions[counts][level] = []
        formatted_question = question['formatted_question']
        orig_nums, orig_ans = question['original_pair']

        for level in levels[1:]:
            nums_questions = random.sample(
                instances[level],
                k=m
            )
            for nums, answer in nums_questions:
                for j, num in enumerate(nums):
                    if not util.is_int(num):
                        nums[j] = round(num, 3)
                new_questions[counts][level].append((formatted_question.format(*nums), answer))
        new_questions[counts]['Originals'] = [formatted_question.format(*orig_nums), orig_ans]
        counts += 1
 
    if len(new_questions) > 0:
        with open(output_file, 'w') as f:
            json.dump(new_questions, f, indent=2)
            print(f"Adversarial examples saved to {output_file}")