# Define the variables
total_students_trying_out = 64
students_not_picked = 36
number_of_groups = 4

# Calculate the number of students picked for the teams
students_picked = total_students_trying_out - students_not_picked

# Calculate the number of students in each group
students_per_group = students_picked // number_of_groups

# Print the final answer
print("Number of students in each group:", students_per_group)