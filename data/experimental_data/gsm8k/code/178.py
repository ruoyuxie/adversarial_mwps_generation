# Define the initial number of marbles Mazie has
total_marbles = 52

# Define the number of marbles Dallas ends up with after dropping some
dallas_marbles_after_drop = 21

# Define the number of marbles Dallas dropped
dallas_dropped_marbles = 4

# Calculate the number of marbles Dallas had before dropping any
dallas_marbles_before_drop = dallas_marbles_after_drop + dallas_dropped_marbles

# Calculate the number of marbles Darla received by subtracting the number Dallas had from the total
darla_marbles = total_marbles - dallas_marbles_before_drop

# Print the final answer
print(f"Darla received {darla_marbles} marbles.")