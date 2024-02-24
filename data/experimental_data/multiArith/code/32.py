# Define variables based on the problem statement
total_rooms_to_paint = 10
hours_per_room = 8
rooms_already_painted = 8

# Calculate the number of rooms left to paint
rooms_left_to_paint = total_rooms_to_paint - rooms_already_painted

# Calculate the total hours needed to paint the remaining rooms
hours_to_paint_remaining_rooms = rooms_left_to_paint * hours_per_room

# Print the final answer
print(f"The painter will take {hours_to_paint_remaining_rooms} more hours to paint the rest of the rooms.")