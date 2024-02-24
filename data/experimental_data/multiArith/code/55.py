# Define the initial variables
total_games = 35
sold_games = 19
games_per_box = 8

# Calculate the remaining games after selling
remaining_games = total_games - sold_games

# Calculate the number of boxes needed
# Since we are not using if-else statements or loops, we'll use integer division
# which will give us the number of full boxes, assuming any leftover games can fit into a partial box
number_of_boxes = (remaining_games + games_per_box - 1) // games_per_box

# Print the final answer
print("Edward had to use", number_of_boxes, "boxes.")