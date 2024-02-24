# Define initial variables based on the problem statement
initial_lives = 10  # Rachel starts with 10 lives
lives_lost = 4      # She loses 4 lives in a hard part of the game
lives_gained = 26   # She gains 26 lives in the next level

# Calculate the remaining lives after losing some
remaining_lives_after_loss = initial_lives - lives_lost

# Calculate the total lives after gaining more lives
total_lives = remaining_lives_after_loss + lives_gained

# Print the final answer
print(f"Rachel would have {total_lives} lives.")