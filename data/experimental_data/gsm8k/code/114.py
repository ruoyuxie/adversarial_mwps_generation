# Define variables
# Let x be George's monthly income
# According to the problem, George donates half of his income and spends $20 from the other half
# He then has $100 left

# Step 1: Calculate the amount left after donating half
# If he donates half, he has half left, so we can represent this as 0.5 * x

# Step 2: Calculate the amount left after spending $20 on groceries
# From the remaining half, he spends $20, so we represent this as (0.5 * x) - 20

# Step 3: Set up the equation based on the fact that he has $100 left
# (0.5 * x) - 20 = 100

# Step 4: Solve for x
# Add 20 to both sides of the equation
# 0.5 * x = 100 + 20

# Step 5: Calculate the total monthly income
# x = (100 + 20) / 0.5

# Perform the calculations
remaining_after_donation = 0.5  # George keeps this fraction after donation
spent_on_groceries = 20  # George spends this amount on groceries
amount_left = 100  # George has this amount left

# Solve for x
x = (amount_left + spent_on_groceries) / remaining_after_donation

# Print the final answer
print(f"George's monthly income was: ${x}")