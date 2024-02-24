# Define the variables
adult_meal_cost = 7  # Cost of each adult meal
total_people = 13    # Total number of people in the group
number_of_kids = 9   # Number of kids in the group

# Calculate the number of adults by subtracting the number of kids from the total people
number_of_adults = total_people - number_of_kids

# Calculate the total cost for the group to eat by multiplying the number of adults by the cost of each adult meal
total_cost = number_of_adults * adult_meal_cost

# Print the final answer
print(f"The total cost for the group to eat is: ${total_cost}")