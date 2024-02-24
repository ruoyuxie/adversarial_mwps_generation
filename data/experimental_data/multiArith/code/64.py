# Define variables for the points scored in each round
first_round_points = 16
second_round_points = 33
last_round_points_lost = 48

# Calculate the total points after all rounds
# Since she lost points in the last round, we subtract that value
total_points = first_round_points + second_round_points - last_round_points_lost

# Print the final answer
print("Emily's final score at the end of the game is:", total_points)