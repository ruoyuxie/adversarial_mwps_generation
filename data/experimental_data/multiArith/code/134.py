# Define the initial number of puppies
total_puppies = 56

# Define the number of puppies sold
puppies_sold = 24

# Calculate the number of puppies left after selling
puppies_left = total_puppies - puppies_sold

# Define the number of puppies per cage
puppies_per_cage = 4

# Calculate the number of cages needed for the remaining puppies
number_of_cages = puppies_left // puppies_per_cage

# Print the final answer
print("The pet store used", number_of_cages, "cages.")