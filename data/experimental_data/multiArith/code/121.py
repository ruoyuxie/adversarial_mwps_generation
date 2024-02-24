# Define initial variables based on the problem statement
initial_lives = 14
lives_lost = 4
lives_gained_next_level = 36

# Calculate the number of lives after losing some
lives_after_loss = initial_lives - lives_lost

# Calculate the total number of lives after gaining more in the next level
total_lives = lives_after_loss + lives_gained_next_level

# Print the final answer
print(f"Haley would have {total_lives} lives.")