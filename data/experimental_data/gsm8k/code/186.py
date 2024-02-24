# Define the total number of brochures
total_brochures = 5000

# Define the fraction of brochures that can fit in one box
fraction_per_box = 1 / 5

# Calculate the number of brochures per box
brochures_per_box = total_brochures * fraction_per_box

# Since each box can only contain a certain number of brochures,
# we need to divide the total number of brochures by the number of brochures per box
# to find out how many boxes are needed.
# We assume that we can only use whole boxes, so we round up to the nearest whole number.
# However, since the fraction is exactly 1/5, we know that the total number of boxes
# will be a whole number without needing to round.

boxes_needed = total_brochures / brochures_per_box

# Print the final answer
print(f"The number of boxes needed to ship the brochures is: {int(boxes_needed)}")