# Define the variables
percentage_made = 80  # Cyrus made 80% of his shots
total_attempts = 20   # Cyrus attempted 20 shots

# Calculate the number of shots made
shots_made = (percentage_made / 100) * total_attempts

# Since we need an integer number of shots, we round down the shots made
shots_made = int(shots_made)

# Calculate the number of missed shots
missed_shots = total_attempts - shots_made

# Print the final answer
print("Cyrus missed", missed_shots, "shots.")