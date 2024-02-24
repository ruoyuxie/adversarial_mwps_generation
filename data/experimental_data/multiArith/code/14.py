# Define the initial number of puppies
total_puppies = 64

# Define the number of puppies sold
puppies_sold = 28

# Calculate the remaining puppies after the sale
remaining_puppies = total_puppies - puppies_sold

# Define the number of puppies per cage
puppies_per_cage = 4

# Calculate the number of cages needed for the remaining puppies
# Since we are looking for the number of whole cages, we use the ceiling division
# to ensure that any remaining puppies, even if less than 4, will get a cage.
import math
number_of_cages = math.ceil(remaining_puppies / puppies_per_cage)

# Print the final answer
print(f"The pet store used {number_of_cages} cages.")