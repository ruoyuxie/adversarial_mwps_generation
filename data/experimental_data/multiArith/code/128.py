# Define the initial number of games
initial_games = 39

# Define the number of games sold
games_sold = 19

# Calculate the remaining games after selling
remaining_games = initial_games - games_sold

# Define the number of games per box
games_per_box = 4

# Calculate the number of boxes needed to pack the remaining games
# Since we are not using if-else statements or loops, we'll use integer division
# to find out how many full boxes we can have and then use the modulo operator
# to check if we need an extra box for the remaining games.
full_boxes = remaining_games // games_per_box
extra_box_needed = remaining_games % games_per_box

# If there are any games left over after filling the full boxes, we need one extra box
total_boxes = full_boxes + (1 if extra_box_needed > 0 else 0)

# Print the final answer
print(f"Luke had to use {total_boxes} boxes.")