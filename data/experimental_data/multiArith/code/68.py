# Define the variables
total_points = 75  # Total points scored by the team
bianca_points = 45  # Points scored by Bianca
other_player_points = 6  # Points scored by each other player

# Calculate the points scored by the rest of the team
rest_of_team_points = total_points - bianca_points

# Calculate the number of other players by dividing the rest of the team's points by the points per player
number_of_other_players = rest_of_team_points // other_player_points

# Bianca is also a player on the team, so we add 1 to include her
total_players = number_of_other_players + 1

# Print the final answer
print(f"The total number of players on Bianca's team is: {total_players}")