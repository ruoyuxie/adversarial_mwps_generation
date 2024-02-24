# Define initial variables
initial_worksheets = 34  # The number of worksheets the teacher initially had
graded_worksheets = 7    # The number of worksheets the teacher graded
new_worksheets = 36      # The number of new worksheets turned in

# Calculate the remaining worksheets after grading some
remaining_worksheets = initial_worksheets - graded_worksheets

# Calculate the total worksheets to grade after new ones are turned in
total_worksheets_to_grade = remaining_worksheets + new_worksheets

# Print the final answer
print("The teacher has to grade", total_worksheets_to_grade, "worksheets.")