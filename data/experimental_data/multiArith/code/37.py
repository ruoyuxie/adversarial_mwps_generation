# Define the variables
total_boxes_bought = 12
boxes_given_away = 7
pieces_per_box = 6

# Calculate the number of boxes Tom has left
boxes_left = total_boxes_bought - boxes_given_away

# Calculate the total number of pieces Tom still has
pieces_left = boxes_left * pieces_per_box

# Print the final answer
print(f"Tom still has {pieces_left} pieces of chocolate candy.")