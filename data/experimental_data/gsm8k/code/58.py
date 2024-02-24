# Define the variables
number_of_carwashes = 20
normal_cost_per_carwash = 15
discount_percentage = 60

# Calculate the total normal cost without the package
total_normal_cost = number_of_carwashes * normal_cost_per_carwash

# Calculate the discount rate as a decimal
discount_rate = discount_percentage / 100

# Calculate the total cost with the package discount
total_discounted_cost = total_normal_cost * discount_rate

# Print the final answer
print("Jim paid", total_discounted_cost, "dollars for the package.")

# If you want to print just the number without text, you can do the following:
print(total_discounted_cost)