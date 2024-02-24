# Define the quantities
regular_sodas = 4
diet_sodas = 52

# Total number of sodas
total_sodas = regular_sodas + diet_sodas

# Capacity of each shelf in the fridge
shelf_capacity = 7

# Calculate the number of shelves needed
# The double slash '//' operator in Python performs integer (floor) division
shelves_needed = total_sodas // shelf_capacity

# If there are any remaining sodas that don't fill up a whole shelf, we need an extra shelf
# The modulo '%' operator gives us the remainder of the division
if total_sodas % shelf_capacity != 0:
    shelves_needed += 1

# Print the final answer
print(f"Tom will fill up {shelves_needed} shelves.")