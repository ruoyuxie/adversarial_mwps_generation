import argparse

# Setup argparse
parser = argparse.ArgumentParser(description='Script Configuration')

# Adding arguments with default values
parser.add_argument('--action', type=str, default="generation", choices=["generation", "analysis"], help='Action to perform: "generation" or "analysis"')
parser.add_argument('--analysis_output_dir', type=str, default="analysis/", help='Directory for analysis output')
parser.add_argument('--generation_output_dir', type=str, default="generated/", help='Directory for generation output')
parser.add_argument('--original_question_file', type=str, default='', help='Original question file path',required=True)
parser.add_argument('--output_file_name', type=str, default='all_temp_generated_example.json', help='Output file name')
parser.add_argument('--code_directory', type=str, default='data/code/', help='Code directory')
parser.add_argument('--attempts', type=int, default=30000, help='Total number of attempts to generate adversarial examples')
parser.add_argument('--processed_file_name', type=str, default="all_temp_processed_example.json", help='Processed file name')
parser.add_argument('--adversarial_file_name', type=str, default="adversarial_example.json", help='Adversarial file name')
parser.add_argument('--m', type=int, default=100, help='number of adversarial examples to generate')
parser.add_argument('--n', type=int, default=5, help='number of problems that have m unique generations')
parser.add_argument('--method', type=int, default=3, help='Generation method. 1 for M1, 2 for M2, 3 for M3. Default is 3 for the best generation quality')
parser.add_argument('--openai_key_path', type=str, default="", help='OpenAI key path')
parser.add_argument('--generate_questions_using_gpt', type=bool, default=True, help='Whether to generate questions using GPT')
parser.add_argument('--distinguish_using_gpt', type=bool, default=False, help='Whether to use GPT for distinguishing variables')
parser.add_argument('--generate_adv_examples', type=bool, default=True, help='Whether to generate adversarial examples')

parser.add_argument('--regression_method', type=str, default='linear', choices=['linear', 'logistic'], help='Regression method for data analysis, "linear" or "logistic"')
parser.add_argument('--model_name', type=str, default="MetaMath-70B-V1.0", help='Model name for feature analysis')
parser.add_argument('--model_incorrect_file', type=str, default='/data/incorrect_results/MetaMath-70B-V1.0.json', help='Model incorrect file path for feature analysis')
parser.add_argument('--graph', type=bool, default=True, help='Whether to show the plots')

# Parse arguments
args = parser.parse_args()

# Set variables with user inputs or default values
action = args.action
analysis_output_dir = args.analysis_output_dir
generation_output_dir = args.generation_output_dir
original_question_file = args.original_question_file
output_file_name = args.output_file_name
code_directory = args.code_directory
counts = args.attempts
processed_file_name = args.processed_file_name
adversarial_file_name = args.adversarial_file_name
n = args.n
m = args.m
method = args.method
openai_key_path = args.openai_key_path
generate_questions_using_gpt = args.generate_questions_using_gpt
distinguish_using_gpt = args.distinguish_using_gpt
generate_adv_examples = args.generate_adv_examples
# The final answer node will have this specific name to ensure no repeating variable name
final_answer_name = "final_answer_variable_name_no_repeat"
regression_method = args.regression_method
model_name = args.model_name
model_incorrect_file = args.model_incorrect_file


output_file_name = generation_output_dir + output_file_name
processed_file_name = generation_output_dir + processed_file_name
adversarial_file_name = generation_output_dir + adversarial_file_name
