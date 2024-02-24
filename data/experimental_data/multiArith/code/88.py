# Define variables
total_customers = 9
customers_who_didnt_tip = 5
tip_per_customer = 8

# Calculate the number of customers who did leave a tip
customers_who_tipped = total_customers - customers_who_didnt_tip

# Calculate the total amount of money earned from tips
total_tips = customers_who_tipped * tip_per_customer

# Print the final answer
print("The waiter earned $", total_tips)