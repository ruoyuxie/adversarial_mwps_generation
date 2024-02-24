# Define the initial number of friends
initial_friends = 10

# Define the number of friends who quit
friends_quit = 7

# Calculate the number of friends remaining
friends_remaining = initial_friends - friends_quit

# Define the number of lives each remaining player has
lives_per_player = 8

# Calculate the total number of lives remaining
total_lives = friends_remaining * lives_per_player

# Print the final answer
print(f"The total number of lives remaining is: {total_lives}")