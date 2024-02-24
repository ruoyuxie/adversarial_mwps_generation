# Define the variables
problems_per_worksheet = 3  # Number of problems on each worksheet
total_worksheets = 15       # Total number of worksheets to grade
graded_worksheets = 7       # Number of worksheets already graded

# Calculate the number of worksheets left to grade
worksheets_left_to_grade = total_worksheets - graded_worksheets

# Calculate the total number of problems left to grade
problems_left_to_grade = worksheets_left_to_grade * problems_per_worksheet

# Print the final answer
print(f"The teacher has {problems_left_to_grade} more problems to grade.")