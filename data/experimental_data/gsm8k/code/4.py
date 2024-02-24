# Define the number of boxes sold on Saturday
boxes_sold_saturday = 60

# Calculate the number of boxes sold on Sunday, which is 50% more than on Saturday
additional_percentage = 50 / 100  # Convert percentage to a decimal
additional_boxes_sunday = boxes_sold_saturday * additional_percentage
boxes_sold_sunday = boxes_sold_saturday + additional_boxes_sunday

# Calculate the total number of boxes sold over the two days
total_boxes_sold = boxes_sold_saturday + boxes_sold_sunday

# Print the final answer
print(f"Tanika sold a total of {int(total_boxes_sold)} boxes over the two days.")