# Define initial quantity of oranges in the bin
initial_oranges = 40

# Define the number of old oranges thrown away
old_oranges_thrown_away = 25

# Define the number of new oranges added to the bin
new_oranges_added = 21

# Calculate the number of oranges remaining after throwing away old ones
oranges_after_throw_away = initial_oranges - old_oranges_thrown_away

# Calculate the final number of oranges in the bin after adding new ones
final_oranges_in_bin = oranges_after_throw_away + new_oranges_added

# Print the final answer
print(f"The final number of oranges in the bin is: {final_oranges_in_bin}")