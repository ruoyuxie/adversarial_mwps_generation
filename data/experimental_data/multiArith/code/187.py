# Define variables for the quantities mentioned in the problem
points_per_treasure = 5  # Wendy scores 5 points for each treasure
treasures_level_1 = 4    # Wendy found 4 treasures on the first level
treasures_level_2 = 3    # Wendy found 3 treasures on the second level

# Calculate the score for each level
score_level_1 = points_per_treasure * treasures_level_1
score_level_2 = points_per_treasure * treasures_level_2

# Calculate the total score by adding the scores from both levels
total_score = score_level_1 + score_level_2

# Print the final answer
print("Wendy's total score is:", total_score)