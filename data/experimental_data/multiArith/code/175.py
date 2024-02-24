# Define the variables
total_clothes = 39
clothes_in_first_load = 19

# Calculate the remaining clothes after the first load
remaining_clothes = total_clothes - clothes_in_first_load

# Define the number of small loads
number_of_small_loads = 5

# Calculate the number of clothes per small load
clothes_per_small_load = remaining_clothes // number_of_small_loads

# Print the final answer
print(f"Each of the small loads can have {clothes_per_small_load} pieces of clothing.")