# Define the variables based on the given problem
total_earnings = 104  # Total money Will made
cost_of_blades = 41   # Money spent on new mower blades
game_price = 9        # Price of each game

# Calculate the money left after buying mower blades
money_left = total_earnings - cost_of_blades

# Calculate the number of games Will can buy
number_of_games = money_left // game_price

# Print the final answer
print("Will can buy", number_of_games, "games with the money he had left.")