# Adversarial Math Word Problem Generation
This is the official repository for [LLM-Resistant Math Word Problem Generation via Adversarial Attacks](https://arxiv.org/abs/). This repository contains the code for generating adversarial math problems, attacking the models, and analyzing the generated adversarial examples.

## Installation
Install all required packages using `pip install -r requirements.txt`.

## Input Data Format 
The original math problems should be formatted in a json file with `"Problem"` and `"final_ans"` fields: 
```sh
[
    {
        "Problem": "<Problem 0>",
        "final_ans": "<Answer 0>"
        ...
    },
    {
        "Problem": "<Problem 1>",
        "final_ans": "<Answer 1>"
        ...
    },
    ...
]
```
An input data example from GSM8K is provided on `data/example/input_example.json`

## Generation
Go to `generation` folder and run `main.py` to generate adversarial examples. The script will call GPT-4-turbo once (~$0.01) for each original problem to generate python code.
Here is an example command for generating `20` adversarial math problems: 
```sh
python main.py \
  --action generation \
  --output_directory ../generated \
  --original_question_file ../data/example/input_example.json \
  --openai_key_path PATH/TO/OPENAI/APIKEY/IN/TXT \
  --code_directory ../data/example/ode \
  --m 20 
```

You can specifiy your own generation settings, file structure/path, etc. in `config.py`. The final generated adversarial examples will be saved in `../generated/adversarial_example.json`. We release all the generated adversarial examples for our experiments in `data/experimental_data` folder.

## Attack 
To attack the models generated adversarial examples, go to `attack` folder and run `attack.py`. An example command for attacking `meta-math/MetaMath-70B-V1.0` is:
```sh
python attack.py \
  --model meta-math/MetaMath-70B-V1.0 \
  --adversarial_data_path ../generated/adversarial_example.json \
  --main_output_directory_path ../results 
```
The model outputs are saved in `../results`. The script will generate model output summary and save it in `model_output_summary` and all incorrect results in `incorrect_problems`. 

## Analysis
To analyze the generated adversarial examples, run `main.py` in the `generation` folder with `--action analysis`. The script will compare model's incorrect predictions with the ground truth. An example command for analyzing `MetaMath-70B-V1.0` is:
```sh
python main.py \
  --action analysis \
  --output_directory ../analysis \
  --model_name MetaMath-70B-V1.0 \
  --model_incorrect_file /data/example/incorrect_problems/MetaMath-70B-V1.0.json 
```
You can specifiy your own analysis settings, show plots, etc. in `config.py`. The final analysis results will be saved in `../analysis/`



## Citation
If you find this code useful, we'd appreciate it if you cite the following paper:
```


```


<!-- 
### Model Response Format
To analyze the output of the models (linear regression on the various features), format the output of the models into
the following json format:
```json
{
  "Originals": {
    "<index>": {
      "problem_index": <index>,
      "problem": "<problem string>", 
      "gold_answer": "<correct answer>", 
      "model_output": "<model output>", 
      "extracted_value": <answer from model>,
      "is_correct": <Boolean indicating extracted_value == gold_answer>
    }, 
    ... more problems
  }, 
  "<generation_methods>": {
    "<index>": {
      "<variant_index>": {
        "problem_index": <index>,
        "problem": "<problem string>", 
        "gold_answer": "<correct answer>", 
        "model_output": "<model output>", 
        "extracted_value": <answer from model>,
        "is_correct": <Boolean indicating extracted_value == gold_answer>
      },
      ... more variants
    },
    ... more problems 
  },
  ... more generation methods
}
``` -->
