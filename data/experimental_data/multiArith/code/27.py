# Define the initial variables
total_games = 76
sold_games = 46
games_per_box = 5

# Calculate the remaining games after selling
remaining_games = total_games - sold_games

# Calculate the number of boxes needed
# Since we are not using if-else statements or loops, we'll use integer division
# to find out how many full boxes he can fill and then use modulo to check if there's a need for an additional box
full_boxes = remaining_games // games_per_box
additional_box = remaining_games % games_per_box > 0

# The total number of boxes is the number of full boxes plus one if there's a need for an additional box
total_boxes = full_boxes + additional_box

# Print the final answer
print("Kaleb had to use", total_boxes, "boxes.")