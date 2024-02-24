# Define the initial number of puppies
total_puppies = 13

# Define the number of puppies sold
puppies_sold = 7

# Calculate the remaining puppies after the sale
remaining_puppies = total_puppies - puppies_sold

# Define the number of puppies per cage
puppies_per_cage = 2

# Calculate the number of cages needed for the remaining puppies
# Since we are putting 2 puppies in each cage, we divide the remaining puppies by 2
# We use the ceil function from the math module to round up to the nearest whole number
# because you can't have a fraction of a cage.
from math import ceil
cages_needed = ceil(remaining_puppies / puppies_per_cage)

# Print the final answer
print(f"The number of cages used is: {cages_needed}")