# Define variables corresponding to the quantities mentioned in the problem
math_homework_pages = 4
reading_homework_pages = 6
problems_per_page = 4

# Calculate the total number of math problems
total_math_problems = math_homework_pages * problems_per_page

# Calculate the total number of reading problems
total_reading_problems = reading_homework_pages * problems_per_page

# Calculate the total number of problems
total_problems = total_math_problems + total_reading_problems

# Print the final answer
print("Sarah had to complete a total of", total_problems, "problems.")