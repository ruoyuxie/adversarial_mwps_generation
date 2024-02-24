# Define the initial number of customers
initial_customers = 22

# Define the number of customers who left
customers_left = 14

# Calculate the number of customers remaining
remaining_customers = initial_customers - customers_left

# Define the number of people at each table
people_per_table = 4

# Calculate the number of tables with the remaining customers
number_of_tables = remaining_customers // people_per_table

# Print the final answer
print("The waiter has", number_of_tables, "tables.")