# Define the weight of each dog
dog1_weight = 20
dog2_weight = 40
dog3_weight = 10
dog4_weight = 30
dog5_weight = 50

# Define the ratio of dog food needed per 10 pounds
food_per_10_pounds = 1

# Calculate the amount of food each dog needs
dog1_food = dog1_weight / 10 * food_per_10_pounds
dog2_food = dog2_weight / 10 * food_per_10_pounds
dog3_food = dog3_weight / 10 * food_per_10_pounds
dog4_food = dog4_weight / 10 * food_per_10_pounds
dog5_food = dog5_weight / 10 * food_per_10_pounds

# Calculate the total amount of food needed for all dogs
total_food_needed = dog1_food + dog2_food + dog3_food + dog4_food + dog5_food

# Print the final answer
print(f"Paul needs {total_food_needed} pounds of dog food each day.")