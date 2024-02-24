# Define the total number of ants
total_ants = 110

# Calculate the number of worker ants (which is half of the total ants)
worker_ants = total_ants / 2

# Calculate the number of male worker ants (which is 20 percent of the worker ants)
male_worker_ants = worker_ants * 0.20

# Calculate the number of female worker ants (which is the rest of the worker ants)
female_worker_ants = worker_ants - male_worker_ants

# Print the final answer
print(f"The number of female worker ants is: {int(female_worker_ants)}")