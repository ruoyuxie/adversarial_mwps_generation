# Define the initial number of apples
total_apples = 47

# Define the number of apples given out to students
apples_given_to_students = 27

# Calculate the remaining apples after giving out to students
remaining_apples = total_apples - apples_given_to_students

# Define the number of apples needed for one pie
apples_per_pie = 4

# Calculate the number of pies that can be made with the remaining apples
number_of_pies = remaining_apples // apples_per_pie

# Print the final answer
print("The cafeteria can make", number_of_pies, "pies.")