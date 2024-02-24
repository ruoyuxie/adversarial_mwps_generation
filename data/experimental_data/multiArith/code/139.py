# Define initial variables
initial_carrots_picked = 28
carrots_thrown_out = 11
carrots_picked_next_day = 9

# Calculate the remaining carrots after throwing out some
remaining_carrots = initial_carrots_picked - carrots_thrown_out

# Calculate the total number of carrots after picking more the next day
total_carrots = remaining_carrots + carrots_picked_next_day

# Print the final answer
print(f"Haley would have {total_carrots} carrots total.")