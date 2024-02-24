# Define the variables for the number of new players and returning players
new_players = 31
returning_players = 4

# Calculate the total number of players
total_players = new_players + returning_players

# Define the number of players per group
players_per_group = 7

# Calculate the number of groups by dividing the total number of players by the number of players per group
# Use integer division to get the number of full groups
number_of_groups = total_players // players_per_group

# Print the final answer
print("The number of groups will be:", number_of_groups)