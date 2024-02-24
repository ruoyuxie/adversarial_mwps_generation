import sys
sys.path.append("../honest_llama")
import argparse
import torch
import pandas as pd
from transformers import LlamaForCausalLM, LlamaTokenizer
#from baukit import Trace, TraceDict
from tqdm import tqdm
import numpy as np
import re
import json
from collections import Counter
import os
import openai
from openai_cost_tracker import query_openai
import random

# set seed
random.seed(42)

def api_key_setup(model):
    if model.__contains__("gpt"):
        openai.api_key = open("/home/users/rx55/projects/keys/openAI_key.txt", "r").read()

instruction = ["", "Solve a math problem."]
enforce_format = ["",
                  'Your final answer should be a single numerical number at the end of your response.',
                  'The solution ends with "the answer is (a number)" like "the answer is 1".',
                  ]
fewshots = ["Qeustion: The state of Virginia had 3.79 inches of rain in March, 4.5 inches of rain in April, 3.95 inches of rain in May, 3.09 inches of rain in June and 4.67 inches in July.  What is the average rainfall amount, in inches, in Virginia?\nAnswer: Let's think step by step. It rained for a total of 3.79+4.5+3.95+3.09+4.67 = 20 inches\nThe rain period is from March through July for a total of 5 months so the average rainfall is 20/5 = 4 inches of rain per month. The answer is 4.\n",
 "Qeustion: A chocolate box contains 200 bars. Thomas and his 4 friends take 1/4 of the bars and decide to divide them equally between them. One of Thomas's friends doesn't like chocolate bars very much and returns 5 of his bars to the box. Later, his sister Piper comes home and takes 5 fewer bars than those taken in total by Thomas and his friends so she can also share with her friends. What's the total number of bars left in the box?\nAnswer: Let's think step by step. Thomas and his friends took 1/4*200 = 50 bars.\nThe total number of bars left in the box was 200-50 = 150 bars.\nSince there are five of them sharing, each of them got 50/5 = 10 bars.\nAfter a friend returned 5 bars, there were 150 + 5 = 155 bars in the box.\nPiper took five fewer bars, that is 50 - 5 = 45 bars.\nThe total remaining bars left in the box is 155 - 45 = 110 bars. The answer is 110.\n",
 "Qeustion: Gilbert grows herbs in his yard to use in his cooking. At the beginning of the spring, he planted three basil bushes, a parsley plant, and two kinds of mint. Halfway through spring, one of the basil plants dropped seeds from a flower and made an extra basil plant grow. However, a rabbit came by the garden near the end of spring and ate all the mint. How many herb plants did Gilbert have when spring ended?\nAnswer: Let's think step by step. Gilbert planted 3 + 1 + 2 = 6 herb plants.\nHe gained a basil plant when one of the basil plants seeded a new plant, so he had 6 + 1 = 7 plants.\nThe rabbit ate both mint plants, so Gilbert had 7 - 2 = 5 herb plants when spring ended. The answer is 5.\n",
 "Qeustion: Marta was about to start the school year and needed to buy the necessary textbooks. She managed to buy five on sale, for $10 each. She had to order two textbooks online, which cost her a total of $40, and three she bought directly from the bookstore for a total of three times the cost of the online ordered books. How much in total did Martha spend on textbooks?\nAnswer: Let's think step by step. Marta bought five textbooks on sale, for a total of 5 * 10 = $50.\nThree textbooks from the bookstore had a cost of 3 * 40 = $120.\nThat means that Marta spent in total 50 + 40 + 120 = $210 on textbooks. The answer is 210.\n",
 "Qeustion: At the burger hut, you can buy a burger for $5, french fries for $3, and a soft drink for $3.  If you order a special burger meal, you get all 3 of these food items for $9.50. A kid’s burger is $3, a kid’s french fries are $2, and a kid's juice box is $2.  They also have a kids meal of all 3 kids' food items for $5. Mr. Parker buys 2 burger meals for his wife and himself.  He also buys 2 burger meals and 2 kid's meals for his 4 children.  How much money does Mr. Parker save by buying the 6 meals versus buying the individual food items?\nAnswer: Let's think step by step. To buy regular food items individually, they cost $5 + $3 + $3 = $11.\nTo buy kids food items individually, they cost $3 + $2 + $2 = $7.\nIf you buy the special burger meal, you save $11 - $9.50 = $1.50.\nIf you buy the kid's meal, you save $7 - $5 = $2.\nMr. Parker buys 4 special burger meals, bringing his discount to 4 x $1.50 = $6.\nHe buys 2 kid's meals, bringing his discount to 2 x $2 = $4.\nThe total savings for Mr. Parker is $6 + $4 = $10. The answer is 10.\n",
 "Qeustion: A roadwork company is paving a newly constructed 16-mile road. They use a mixture of pitch and gravel to make the asphalt to pave the road. Each truckloads of asphalt uses two bags of gravel and five times as many bags of gravel as it does barrels of pitch to make. It takes three truckloads of asphalt to pave each mile of road. The company paved 4 miles of road on one day, then one mile less than double that on the second day. How many barrels of pitch will the company need to finish the remaining road on the third day?\nAnswer: Let's think step by step. On the second day, the company paved 4 * 2 - 1 = 7 miles.\nThe company has 16 - 7 - 4 = 5 miles of road remaining to pave.\nThey will need 3 * 5 = 15 truckloads of asphalt to pave 5 miles of road.\nFor 15 truckloads, they will need 15 * 2 = 30 bags of gravel.\nThus, the company will need 30 / 5 = 6 barrels of pitch to finish the road on the third day. The answer is 6.\n",
 "Qeustion: Nancy wanted to make peanut butter cookies for a family gathering, but her cousin is allergic to peanuts. She decided to make almond butter cookies instead. A jar of almond butter costs three times the amount that a jar of peanut butter does. It takes half a jar to make a batch of cookies. A jar of peanut butter costs $3. How many dollars more does it cost per batch to make almond butter cookies instead of peanut butter cookies?\nAnswer: Let's think step by step. A jar of almond butter costs 3 * 3 = $9.\nIt takes half a jar to make a batch of cookies, so it costs 9 / 2 = $4.50 to use almond butter.\nIt costs 3 / 2 = $1.50 to use peanut butter.\nThus, it costs 4.50 - 1.50 = $3 more to make a batch of almond butter cookies than peanut butter cookies. The answer is 3.\n",
 "Qeustion: Barry goes to a shop to buy a shirt he'd been admiring for quite some time. He tells the attendant that it's his birthday so she decides to give him a 15% special discount. The price tag on the shirt says $80. How much is he supposed to pay now, considering the special discount?\nAnswer: Let's think step by step. 15% of $80 = (15/100)*$80 = $12\nThe dollar amount of the discount is $12 so he is supposed to pay just $80-$12 = $68. The answer is 68.\n"]

DATASET_PATHS = "/usr/xtmp/jw834/saved/probing/datasets"
save_dir = "/usr/xtmp/jw834/saved/probing/results"

HF_NAMES = {
    'llama_7B': 'baffo32/decapoda-research-llama-7B-hf',
    'honest_llama_7B': 'validation/results_dump/llama_7B_seed_42_top_48_heads_alpha_15',
    'alpaca_7B': 'circulus/alpaca-7b', 
    'vicuna_7B': 'AlekseyKorshuk/vicuna-7b', 
    'llama2_7B': 'meta-llama/Llama-2-7b-hf', 
    'llama2_13B': 'meta-llama/Llama-2-13b-hf', 
    'llama2_70B': 'meta-llama/Llama-2-70b-hf', 
    'llama2_chat_7B': 'meta-llama/Llama-2-7b-chat-hf', 
    'llama2_chat_13B': 'meta-llama/Llama-2-13b-chat-hf', 
    'llama2_chat_70B': 'meta-llama/Llama-2-70b-chat-hf', 
}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('model_name', type=str, default='llama2_13B')
    parser.add_argument('dataset_name', type=str, default='gsm8k')
    parser.add_argument('--shot', type=int, default=0)
    parser.add_argument('--device', type=int, default=0)
    parser.add_argument('--sc', type=int, default=1)
    parser.add_argument('--temperature', type=float, default=0)
    parser.add_argument('--n', type=int, default=1)
    parser.add_argument('--eformat', type=int, default=1)
    parser.add_argument('--cot', action='store_true', default=False, help='whether to use cot')
    parser.add_argument("--model_dir", type=str, default=None, help='local directory with model data')
    args = parser.parse_args()
    return args

def load_model(args):
    if "gpt" in args.model_name:
        return None, args.model_name, None
    MODEL = HF_NAMES[args.model_name] if not args.model_dir else args.model_dir
    tokenizer = LlamaTokenizer.from_pretrained(MODEL)
    model = LlamaForCausalLM.from_pretrained(MODEL, low_cpu_mem_usage=True, torch_dtype=torch.float16, device_map="auto")
    device = "cuda"
    # print(tokenizer.pad_token_id, tokenizer.bos_token_id)
    tokenizer.pad_token_id = 0 if tokenizer.pad_token_id is None else tokenizer.pad_token_id

    return tokenizer, model, device

# def load_dataset(args):
#     lines = json.load(open(f"/usr/project/xtmp/rx55/projects/aallm/src/main/data/formatted_gsm8k.json"))
#     return lines

def load_dataset(args):
    with open("/usr/project/xtmp/rx55/projects/aallm/src/main/data/test.jsonl") as f:
        lines = f.readlines()
        lines = [json.loads(line) for line in lines]

        # randomly select 100 examples
        random.shuffle(lines)
        lines = lines[:100]

    return lines

def extractAnswer(answer):
    numbers = re.findall(r"\d+\.?\,?\d*", answer)
    if len(numbers)==0:
        return -9999
    else:
        solution = re.sub(r"[^0-9.]", "", numbers[-1])
        return solution
    
    
def get_llama_response(args,prompt,tokenizer,model,device):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    if not hasattr(args, 'temperature'):
        args.temperature = 0
    if not hasattr(args, 'n'):
        args.n = 1
    do_sample = args.n > 1
    output = model.generate(**inputs, do_sample=do_sample, 
                            max_new_tokens=512, temperature=args.temperature,
                            num_return_sequences=args.n)
    responses = tokenizer.batch_decode(output, skip_special_tokens=True)
    # only get the extra generated part
    responses = [response[len(prompt):] for response in responses]
    return responses
def get_chatgpt_response(args,prompt,model):
    message = [{"role":"user","content":prompt}]
    response = query_openai(
        model=model,
        messages=message,
        temperature=args.temperature,
        max_tokens=512,
        n=args.n,
    )
    responses = [message.message.content for message in response.choices]
    return responses
def get_response(args,prompt,tokenizer,model,device):
    if "gpt" in args.model_name:
        return get_chatgpt_response(args,prompt,model)
    else:
        return get_llama_response(args,prompt,tokenizer,model,device)

def format_prompt(question, args):
    cot = ""
    if args.cot:
        cot = " Let's think step by step."
    if args.shot > 0:
        fewshot_examples = fewshots[:args.shot]
        fewshot_examples = "\n".join(fewshot_examples)
        prompt = f"{instruction[1]} {enforce_format[args.eformat]}\n{fewshot_examples}\nQuestion: {question}\nAnswer:{cot if args.cot else ''}"
    else:
        prompt = f"{instruction[1]} {enforce_format[args.eformat]}\nQuestion: {question}\nAnswer:{cot if args.cot else ''}"
    return prompt

def self_consistency(predictions,target,sc=1):
    if sc <= 1:
        return predictions[0]==target
    else:
        answer_counts = Counter(predictions[:sc])
        return answer_counts.most_common(1)[0][0] == target
    
if __name__ == "__main__":
    api_key_setup("llama_70B")

    args = get_args()
    dataset = load_dataset(args)
    print(f"Loaded {len(dataset)} examples from {args.dataset_name}")
    correct = 0
    answers = []
    tokenizer, model, device = load_model(args)

    for i in tqdm(range(len(dataset))):
        print(i)
        question = dataset[i]['question']
        label = dataset[i]['answer']
        digit_label = label.split("\n#### ")[1]
        digit_label = extractAnswer(digit_label)
        prompt = format_prompt(question, args)
        if i == 0:
            print("-----sample prompt:")
            print(prompt)
            print("------")
        responses = get_response(args,prompt,tokenizer,model,device)
        print("\n============\n".join(responses))
        digit_answers = [float(extractAnswer(x)) for x in responses]
        print(digit_answers, float(digit_label))
        answers.append({"question": question, "prompt":prompt,"label": digit_label, "response": responses, "answer": digit_answers})
        correct += self_consistency(digit_answers, float(digit_label), args.sc)
    print(f"Accuracy: {correct/len(dataset)}")
    #save_path = f'{save_dir}/{args.dataset_name}_{args.model_name}_{args.shot}_{"CoT" if args.cot else ""}_enforce{args.eformat}_n{args.n}_temp{args.temperature}.jsonl'
    save_path = f"/usr/project/xtmp/rx55/projects/aallm/src/main/data/gsm8k_test_results_{model}.jsonl"
    print(f"Saving results to {save_path}")
    with open(save_path, "w") as f:
        for answer in answers:
            f.write(json.dumps(answer)+"\n")


# py /usr/project/xtmp/rx55/projects/aallm/src/main/scripts/reasoning_results.py --eformat 2 --cot llama2_70B gsm8k