# Define the variables
pies_needed = 10
apples_per_pie = 8
apples_harvested = 50

# Calculate the total number of apples needed for the pies
total_apples_needed = pies_needed * apples_per_pie

# Calculate the number of apples Mary needs to buy
apples_to_buy = total_apples_needed - apples_harvested

# Check if Mary needs to buy more apples
if apples_to_buy < 0:
    apples_to_buy = 0

# Print the final answer
print(f"Mary needs to buy {apples_to_buy} more apples to make all {pies_needed} pies.")