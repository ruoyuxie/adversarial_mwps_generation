# Define variables
total_invited = 24
no_show = 10
table_capacity = 7

# Calculate the number of people who showed up
people_showed_up = total_invited - no_show

# Calculate the number of tables needed
# The number of tables is the ceiling of the number of people divided by the table capacity
# Since we can't have a fraction of a table, we round up to the nearest whole number
tables_needed = -(-people_showed_up // table_capacity)  # This is a way to do ceiling division without using if-else or loops

# Print the final answer
print(f"The number of tables needed is: {tables_needed}")