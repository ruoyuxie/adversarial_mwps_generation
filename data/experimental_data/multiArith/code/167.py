# Define the variables
flowers_per_vase = 6
carnations = 7
roses = 47

# Calculate the total number of flowers
total_flowers = carnations + roses

# Calculate the number of vases needed
# Since we can't have a fraction of a vase, we use the ceiling division to round up
vases_needed = -(-total_flowers // flowers_per_vase)

# Print the final answer
print(f"Number of vases needed: {vases_needed}")