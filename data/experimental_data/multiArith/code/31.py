# Define the variables for the quantities mentioned in the problem
short_sleeve_shirts = 9
long_sleeve_shirts = 27
total_shirts_washed_before_school = 20

# Calculate the total number of shirts Dave had to wash
total_shirts_to_wash = short_sleeve_shirts + long_sleeve_shirts

# Calculate the number of shirts Dave did not wash before school started
shirts_not_washed = total_shirts_to_wash - total_shirts_washed_before_school

# Print the final answer
print(f"Dave did not wash {shirts_not_washed} shirts before school started.")