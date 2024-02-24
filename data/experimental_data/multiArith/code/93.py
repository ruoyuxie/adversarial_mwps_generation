# Define initial variables based on the problem statement
initial_carrots_picked = 19
carrots_thrown_out = 4
carrots_picked_next_day = 46

# Calculate the number of carrots after throwing out some
carrots_after_throw_out = initial_carrots_picked - carrots_thrown_out

# Calculate the total number of carrots after picking more the next day
total_carrots = carrots_after_throw_out + carrots_picked_next_day

# Print the final answer
print(f"Megan would have a total of {total_carrots} carrots.")