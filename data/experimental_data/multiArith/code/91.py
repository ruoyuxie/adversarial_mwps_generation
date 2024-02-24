# Define variables for the quantities mentioned in the problem
points_per_treasure = 9  # Rachel scores 9 points for each treasure
treasures_level_1 = 5    # Number of treasures found on the first level
treasures_level_2 = 2    # Number of treasures found on the second level

# Calculate the score for each level
score_level_1 = points_per_treasure * treasures_level_1
score_level_2 = points_per_treasure * treasures_level_2

# Calculate the total score by adding the scores from both levels
total_score = score_level_1 + score_level_2

# Print the final answer
print("Rachel's total score is:", total_score)