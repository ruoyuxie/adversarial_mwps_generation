# Define the initial number of friends
initial_friends = 10

# Define the number of friends who dropped out
dropped_out_friends = 4

# Define the remaining number of friends
remaining_friends = initial_friends - dropped_out_friends

# Define the increase in each share
increase_per_share = 8

# Calculate the total increase in cost for the remaining friends
total_increase = increase_per_share * remaining_friends

# Calculate the original share per friend before the drop out
original_share = total_increase / dropped_out_friends

# Calculate the total cost of the gift
total_cost = original_share * initial_friends

# Print the final answer
print(f"The total cost of the gift is: ${total_cost}")