# Define variables based on the problem statement
dollars_per_lawn = 9  # Roger earns $9 for each lawn
total_lawns = 14      # Total lawns Roger had to mow
forgotten_lawns = 8   # Lawns Roger forgot to mow

# Calculate the number of lawns Roger actually mowed
lawns_mowed = total_lawns - forgotten_lawns

# Calculate the total earnings for the lawns Roger mowed
total_earnings = lawns_mowed * dollars_per_lawn

# Print the final answer
print("Roger actually earned:", total_earnings)