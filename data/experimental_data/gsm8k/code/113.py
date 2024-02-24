# Define the variables
number_of_nuggets_ordered = 100  # The total number of chicken nuggets Mark orders
nuggets_per_box = 20             # The number of chicken nuggets in one box
cost_per_box = 4                 # The cost of one box of chicken nuggets in dollars

# Calculate the number of boxes needed
# Since we are avoiding modulo operations, we'll use integer division
number_of_boxes_needed = number_of_nuggets_ordered // nuggets_per_box

# Calculate the total cost
total_cost = number_of_boxes_needed * cost_per_box

# Print the final answer
print("Mark paid $" + str(total_cost) + " for the chicken nuggets.")