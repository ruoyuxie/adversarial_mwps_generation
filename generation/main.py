import os.path

from question_generation import generate_instances_of_questions, post_process, choose_random_from_given_level
import config
from gpt_code_prompt import main_process
from regression import regression_main
import plot

if __name__ == "__main__":

    if config.action == "generation":

        if not os.path.exists(config.generation_output_dir):
            os.makedirs(config.generation_output_dir)                   

        # Prompt GPT to generate codes for questions, undertaking this step involves charges to GPT
        if config.generate_questions_using_gpt:
            main_process(config.original_question_file, config.code_directory, config.openai_key_path)

        # Generates problems (including problems that don't follow the constraints)
        if config.generate_adv_examples:
            generate_instances_of_questions(
                config.original_question_file,
                config.output_file_name,
                config.code_directory,
                counts=config.counts,
                level=config.method
            )

        # Post-processing filters out problems that don't follow the constraints
        post_process(config.output_file_name, config.processed_file_name)

        # Chooses n random questions, with each level having m unique generations
        choose_random_from_given_level(
            config.processed_file_name,
            config.adversarial_file_name,
            n=config.n,
            m=config.m,
            level=config.method

        )

    elif config.action == "analysis":
        if not os.path.exists(config.analysis_output_dir):
            os.makedirs(config.analysis_output_dir)

        # Analyze feature results
        regression_main(method=config.regression_method)

        # Show the plots, only for linear regression
        if config.graph:
            plot.main(regression_method=config.regression_method)
