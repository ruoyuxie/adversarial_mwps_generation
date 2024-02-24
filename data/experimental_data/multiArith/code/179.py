# Define variables based on the problem statement
dollars_per_lawn = 4  # Edward earns 4 dollars for each lawn
total_lawns = 17      # Total lawns he had to mow
forgotten_lawns = 9   # Lawns he forgot to mow

# Calculate the number of lawns he actually mowed
lawns_mowed = total_lawns - forgotten_lawns

# Calculate the total earnings
earnings = lawns_mowed * dollars_per_lawn

# Print the final answer
print(f"Edward actually earned ${earnings}.")