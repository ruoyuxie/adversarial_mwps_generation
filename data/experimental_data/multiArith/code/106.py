# Define initial variables
initial_worksheets = 38  # The number of worksheets the teacher initially had
graded_worksheets = 4    # The number of worksheets the teacher graded
new_worksheets = 15      # The number of new worksheets turned in

# Calculate the remaining worksheets to grade
# Subtract the graded worksheets from the initial count and add the new worksheets
remaining_worksheets = initial_worksheets - graded_worksheets + new_worksheets

# Print the final answer
print(f"The teacher has {remaining_worksheets} worksheets to grade.")