# Define initial number of people in line
initial_people_in_line = 10

# Define the number of people who got tired and left
people_left = 2

# Define the number of new people who got in line
new_people_in_line = 2

# Calculate the final number of people in line
# Since the number of people who left is the same as the number of new people,
# the final number of people in line remains unchanged.
final_people_in_line = initial_people_in_line - people_left + new_people_in_line

# Print the final answer
print(f"The final number of people in line is: {final_people_in_line}")