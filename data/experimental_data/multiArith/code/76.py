# Define initial number of customers
initial_customers = 14

# Define the number of customers that left
customers_left = 3

# Define the number of new customers that arrived
new_customers = 39

# Calculate the number of customers after some left
current_customers = initial_customers - customers_left

# Calculate the final number of customers after new ones arrived
final_customers = current_customers + new_customers

# Print the final answer
print(f"The waiter has {final_customers} customers.")