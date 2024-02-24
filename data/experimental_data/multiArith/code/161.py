# Define initial variables
initial_puppies = 5
new_puppies = 35
adoption_rate_per_day = 8

# Calculate the total number of puppies
total_puppies = initial_puppies + new_puppies

# Calculate the number of days it would take for all puppies to be adopted
days_to_adopt_all = total_puppies / adoption_rate_per_day

# Print the final answer
print(f"It would take {days_to_adopt_all} days for all the puppies to be adopted.")