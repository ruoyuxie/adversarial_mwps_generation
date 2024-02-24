# Define the initial number of apples
total_apples = 96

# Define the number of apples handed out to students
apples_handed_out = 42

# Calculate the remaining apples after handing out
remaining_apples = total_apples - apples_handed_out

# Define the number of apples needed for one pie
apples_per_pie = 6

# Calculate the number of pies that can be made
number_of_pies = remaining_apples // apples_per_pie

# Print the final answer
print("The cafeteria can make", number_of_pies, "pies.")