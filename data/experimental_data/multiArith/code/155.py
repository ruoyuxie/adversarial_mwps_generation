# Define the variables
clothes_per_load = 8
total_shirts = 39
total_sweaters = 33

# Calculate the total number of clothes
total_clothes = total_shirts + total_sweaters

# Calculate the number of loads needed
# Since we can't have a fraction of a load, we use the ceiling division to round up
number_of_loads = -(-total_clothes // clothes_per_load)

# Print the final answer
print(f"Wendy would have to do {number_of_loads} loads.")