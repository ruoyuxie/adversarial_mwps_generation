# Define the variables
number_of_bars = 20
weight_per_bar = 1.5  # in pounds
cost_per_pound = 0.5  # in dollars

# Calculate the total weight of the soap
total_weight = number_of_bars * weight_per_bar

# Calculate the total cost
total_cost = total_weight * cost_per_pound

# Print the final answer
print("John spent ${:.2f} on soap.".format(total_cost))