# Define the variables
points_per_enemy = 9
total_enemies = 11
enemies_left = 3

# Calculate the number of enemies defeated
enemies_defeated = total_enemies - enemies_left

# Calculate the total points earned
total_points = enemies_defeated * points_per_enemy

# Print the final answer
print(f"The total points earned is: {total_points}")