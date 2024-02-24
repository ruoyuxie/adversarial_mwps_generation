# Define the variables
total_potatoes = 15  # Total number of potatoes the chef needs to cook
cooked_potatoes = 6  # Number of potatoes already cooked
cooking_time_per_potato = 8  # Time in minutes it takes to cook one potato

# Calculate the number of potatoes left to cook
potatoes_left_to_cook = total_potatoes - cooked_potatoes

# Calculate the total cooking time for the remaining potatoes
total_cooking_time = potatoes_left_to_cook * cooking_time_per_potato

# Print the final answer
print(f"The time it will take to cook the rest of the potatoes is: {total_cooking_time} minutes.")