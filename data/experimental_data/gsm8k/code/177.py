# Define the variables
total_lessons = 10  # Total number of dance lessons Tom decides to take
cost_per_lesson = 10  # Cost of each dance lesson in dollars
free_lessons = 2  # Number of dance lessons Tom gets for free

# Calculate the number of paid lessons
paid_lessons = total_lessons - free_lessons

# Calculate the total cost
total_cost = paid_lessons * cost_per_lesson

# Print the final answer
print("Tom pays a total of $" + str(total_cost) + " for the dance lessons.")