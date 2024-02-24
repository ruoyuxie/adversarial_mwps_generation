# Define variables
silver_coins = None  # We don't know the exact number of silver coins yet
gold_coins = 70  # Given number of gold coins

# According to the problem, there are 30 more gold coins than silver coins
# So we can express the number of silver coins in terms of gold coins
silver_coins = gold_coins - 30

# Now we calculate the total number of coins
total_coins = gold_coins + silver_coins

# Print the final answer
print("Gretchen has a total of", total_coins, "coins.")