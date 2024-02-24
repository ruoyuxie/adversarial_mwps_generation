# Define the variables
problems_per_worksheet = 7
total_worksheets = 17
graded_worksheets = 8

# Calculate the number of worksheets left to grade
worksheets_left_to_grade = total_worksheets - graded_worksheets

# Calculate the number of problems left to grade
problems_left_to_grade = worksheets_left_to_grade * problems_per_worksheet

# Print the final answer
print(f"The teacher has {problems_left_to_grade} more problems to grade.")