# Define the initial number of cakes
total_cakes = 12

# A crow knocks over half of the stack
cakes_knocked_over = total_cakes // 2

# Chastity picks up half of the fallen cakes, which are not damaged
cakes_saved = cakes_knocked_over // 2

# Calculate the number of cakes destroyed
cakes_destroyed = cakes_knocked_over - cakes_saved

# Print the final answer
print(f"The number of cakes destroyed is: {cakes_destroyed}")