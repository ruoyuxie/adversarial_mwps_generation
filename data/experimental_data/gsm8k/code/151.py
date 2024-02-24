# Define the variables based on the problem statement
number_of_tshirts = 5
cost_per_tshirt = 100
number_of_pants = 4
total_cost = 1500

# Calculate the total cost of t-shirts
total_cost_of_tshirts = number_of_tshirts * cost_per_tshirt

# Subtract the total cost of t-shirts from the total cost to find the total cost of pants
total_cost_of_pants = total_cost - total_cost_of_tshirts

# Calculate the cost of each pair of pants
cost_per_pant = total_cost_of_pants / number_of_pants

# Print the final answer
print(f"The cost of each pair of pants is: ${cost_per_pant}")