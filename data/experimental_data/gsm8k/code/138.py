# Define the quantities in dozens
dozen = 12
benjamin_eggs_dozen = 6
carla_multiplier = 3
trisha_less_dozen = 4

# Calculate the number of eggs each person collects in dozens
benjamin_eggs = benjamin_eggs_dozen * dozen
carla_eggs = carla_multiplier * benjamin_eggs
trisha_eggs = (benjamin_eggs_dozen - trisha_less_dozen) * dozen

# Calculate the total number of eggs collected by all three in dozens
total_eggs = benjamin_eggs + carla_eggs + trisha_eggs

# Convert the total number of eggs back to dozens
total_dozen = total_eggs // dozen

# Print the final answer
print(f"The three collect a total of {total_dozen} dozen eggs.")