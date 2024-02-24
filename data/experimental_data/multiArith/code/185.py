# Define initial variables
initial_amount = 57  # Will's initial amount in dollars
game_cost = 27       # Cost of the new game in dollars
toy_cost = 6         # Cost of each toy in dollars

# Calculate the remaining amount after buying the game
remaining_amount = initial_amount - game_cost

# Calculate the number of toys Will can buy with the remaining amount
number_of_toys = remaining_amount // toy_cost

# Print the final answer
print("Will can buy", number_of_toys, "toys with the money he has left.")