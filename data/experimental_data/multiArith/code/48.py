# Define the variables
points_per_enemy = 8  # Points earned per defeated enemy
total_enemies = 7     # Total number of enemies in the level
enemies_left = 2      # Number of enemies left undefeated

# Calculate the number of enemies defeated
enemies_defeated = total_enemies - enemies_left

# Calculate the total points earned
total_points = points_per_enemy * enemies_defeated

# Print the final answer
print(f"The total points earned is: {total_points}")