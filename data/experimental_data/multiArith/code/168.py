# Define the variables
total_students_trying_out = 58
students_not_picked = 10
number_of_groups = 8

# Calculate the number of students that got picked
students_picked = total_students_trying_out - students_not_picked

# Calculate the number of students in each group
students_per_group = students_picked // number_of_groups

# Print the final answer
print("Number of students in each group:", students_per_group)