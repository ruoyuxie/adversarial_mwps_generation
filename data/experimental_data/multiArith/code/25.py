# Define initial variables based on the problem statement
initial_customers = 39
additional_customers_during_rush = 12
customers_who_didnt_tip = 49

# Calculate the total number of customers the waiter had
total_customers = initial_customers + additional_customers_during_rush

# Calculate the number of customers who left a tip
customers_who_tipped = total_customers - customers_who_didnt_tip

# Print the final answer
print(f"The number of customers who left a tip is: {customers_who_tipped}")