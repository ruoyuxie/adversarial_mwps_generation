# Define the initial number of friends
initial_friends = 8

# Define the number of friends who quit
friends_quit = 3

# Define the number of lives each remaining player has
lives_per_player = 3

# Calculate the number of friends remaining after some quit
remaining_friends = initial_friends - friends_quit

# Calculate the total number of lives remaining
total_lives = remaining_friends * lives_per_player

# Print the final answer
print("Total lives remaining:", total_lives)