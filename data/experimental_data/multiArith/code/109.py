# Define variables based on the given problem
total_earnings = 19  # Frank's total earnings from mowing lawns
cost_of_blades = 11  # Cost of buying new mower blades
game_price = 2       # Price of each game

# Calculate the remaining money after buying mower blades
remaining_money = total_earnings - cost_of_blades

# Calculate the number of games Frank can buy with the remaining money
number_of_games = remaining_money // game_price

# Print the final answer
print("Frank can buy", number_of_games, "games with the money he had left.")