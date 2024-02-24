# Define the initial number of friends
initial_friends = 8

# Define the number of friends that joined later
friends_joined = 2

# Define the number of lives each player has
lives_per_player = 6

# Calculate the total number of friends after the new players joined
total_friends = initial_friends + friends_joined

# Calculate the total number of lives for all players
total_lives = total_friends * lives_per_player

# Print the final answer
print(f"The total number of lives the players have is: {total_lives}")