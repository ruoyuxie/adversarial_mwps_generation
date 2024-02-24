# Define the variables based on the given problem
tables = 7
women_per_table = 7
men_per_table = 2

# Calculate the number of customers per table
customers_per_table = women_per_table + men_per_table

# Calculate the total number of customers the waiter had
total_customers = tables * customers_per_table

# Print the final answer
print("The waiter had a total of", total_customers, "customers.")