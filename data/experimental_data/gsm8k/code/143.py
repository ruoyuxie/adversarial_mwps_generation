# Define the initial number of daisies Kylie has
initial_daisies = 5

# Define the number of daisies given by her sister
daisies_from_sister = 9

# Calculate the total number of daisies after receiving more from her sister
total_daisies = initial_daisies + daisies_from_sister

# Calculate the number of daisies Kylie gives to her mother
daisies_to_mother = total_daisies // 2  # Using integer division to avoid using modulo

# Calculate the number of daisies Kylie has left
daisies_left = total_daisies - daisies_to_mother

# Print the final answer
print(f"Kylie has {daisies_left} daisies left.")