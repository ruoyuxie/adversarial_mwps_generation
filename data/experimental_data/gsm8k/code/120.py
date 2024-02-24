# Define the number of eggs laid each day
first_day_eggs = 50
second_day_eggs = first_day_eggs * 2  # The second day, she doubles her production
third_day_eggs = second_day_eggs + 20  # The third day, she lays 20 more than the second day

# Calculate the total number of eggs laid in the first three days
first_three_days_total = first_day_eggs + second_day_eggs + third_day_eggs

# The last day, she doubles the first three days total
fourth_day_eggs = first_three_days_total * 2

# Calculate the total number of eggs laid over the span of 4 days
total_eggs = first_three_days_total + fourth_day_eggs

# Print the final answer
print("The frog laid a total of", total_eggs, "eggs over the span of 4 days.")