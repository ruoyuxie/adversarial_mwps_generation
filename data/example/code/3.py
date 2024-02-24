# Define variables based on the problem statement
cost_per_charm = 15  # Cost of each charm in dollars
charms_per_necklace = 10  # Number of charms used to make one necklace
selling_price_per_necklace = 200  # Selling price of one necklace in dollars
necklaces_sold = 30  # Number of necklaces sold

# Calculate the cost to make one necklace
cost_to_make_one_necklace = cost_per_charm * charms_per_necklace

# Calculate the profit made from selling one necklace
profit_per_necklace = selling_price_per_necklace - cost_to_make_one_necklace

# Calculate the total profit from selling all necklaces
total_profit = profit_per_necklace * necklaces_sold

# Print the final answer
print("Total profit from selling", necklaces_sold, "necklaces is $", total_profit)