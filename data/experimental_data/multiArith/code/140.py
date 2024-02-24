# Define the variables based on the quantities mentioned in the problem
games_bought_from_friend = 50
games_bought_at_garage_sale = 27
non_working_games = 74

# Calculate the total number of games bought
total_games_bought = games_bought_from_friend + games_bought_at_garage_sale

# Calculate the number of good working games
good_games = total_games_bought - non_working_games

# Print the final answer
print(f"Ned ended up with {good_games} good games.")