# Define the variables
cost_per_dozen = 5  # dollars
total_spent = 15    # dollars

# Calculate the number of dozens John can buy
dozens_bought = total_spent / cost_per_dozen

# Calculate the total number of rolls
# Since a dozen is 12 rolls, we multiply the dozens by 12
rolls_per_dozen = 12
total_rolls = dozens_bought * rolls_per_dozen

# Print the final answer
print(f"John got {int(total_rolls)} rolls.")