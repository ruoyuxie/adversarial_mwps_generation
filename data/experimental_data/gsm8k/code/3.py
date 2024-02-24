# Define the initial variables
students_per_group = 8  # Number of students in each group
number_of_groups = 3    # Total number of groups
students_left_early = 2 # Number of students who left early

# Calculate the total number of students before any left
total_students_initially = students_per_group * number_of_groups

# Calculate the number of students remaining after some left early
students_remaining = total_students_initially - students_left_early

# Print the final answer
print("The number of students remaining is:", students_remaining)