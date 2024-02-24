# Define the variables based on the problem statement
feet_of_dock = 200  # Total feet of dock
line_per_foot_of_dock = 3  # The amount of line needed per foot of dock
current_line = 6  # The amount of line the caretaker already has

# Calculate the total amount of line needed
total_line_needed = feet_of_dock * line_per_foot_of_dock

# Calculate the amount of line the caretaker needs to buy
line_to_buy = total_line_needed - current_line

# Print the final answer
print(f"The caretaker needs to buy {line_to_buy} feet of line in total.")

# Verify the answer
assert line_to_buy == 594, f"Expected 594, but got {line_to_buy}"