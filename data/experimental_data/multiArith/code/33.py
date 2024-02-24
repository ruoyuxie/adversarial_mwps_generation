# Define the variables
total_points = 41  # Total points scored by the team
paige_points = 11  # Points scored by Paige
other_player_points = 6  # Points scored by each other player

# Calculate the points scored by the rest of the team
rest_of_team_points = total_points - paige_points

# Calculate the number of other players on the team
# Since each other player scored 6 points, divide the rest of the team's points by 6
number_of_other_players = rest_of_team_points // other_player_points

# Calculate the total number of players on the team
# Add Paige to the number of other players
total_players = number_of_other_players + 1

# Print the final answer
print("Number of players on Paige's team:", total_players)