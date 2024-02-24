# Define variables
apples_per_bag = 10  # number of apples in one bag
total_apples_sold = 2000  # total number of apples sold
price_per_bag = 5  # price of one bag of apples in dollars

# Calculate the number of bags sold
# Since we know that each bag contains 10 apples, we can find the number of bags by dividing the total apples sold by the number of apples per bag.
# We avoid using modulo operations and assume that the total apples sold is a multiple of apples_per_bag as per the problem statement.
bags_sold = total_apples_sold // apples_per_bag

# Calculate the total earnings
# The total earnings are calculated by multiplying the number of bags sold by the price per bag.
total_earnings = bags_sold * price_per_bag

# Print the final answer
print("The orchard earned $", total_earnings, " for selling ", total_apples_sold, " apples.", sep='')

# Output should be: The orchard earned $1000 for selling 2000 apples.