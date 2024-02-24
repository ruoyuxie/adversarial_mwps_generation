# Define the variables
total_boxes_bought = 12
boxes_given_away = 5
pieces_per_box = 3

# Calculate the number of boxes Dave has left
boxes_left = total_boxes_bought - boxes_given_away

# Calculate the total number of pieces Dave still has
pieces_left = boxes_left * pieces_per_box

# Print the final answer
print(f"Dave still has {pieces_left} pieces of chocolate candy.")