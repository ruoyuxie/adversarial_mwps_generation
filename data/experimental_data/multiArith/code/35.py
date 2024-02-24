# Define the initial variables
total_clothing = 47
first_load = 17

# Calculate the remaining pieces after the first load
remaining_clothing = total_clothing - first_load

# Define the number of small loads
number_of_small_loads = 5

# Calculate the number of pieces per small load
pieces_per_small_load = remaining_clothing // number_of_small_loads

# Print the final answer
print(f"Each of the small loads can have {pieces_per_small_load} pieces of clothing.")