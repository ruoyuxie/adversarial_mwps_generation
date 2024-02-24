# Define initial variables
initial_bears = 17  # Number of bears in stock initially
shipment_bears = 10  # Number of bears in the new shipment
bears_per_shelf = 9  # Number of bears that fit on each shelf

# Calculate the total number of bears after the shipment
total_bears = initial_bears + shipment_bears

# Calculate the number of shelves used
# Since we are not using if-else statements or loops, we'll use integer division
# which will give us the number of full shelves used. If there are any remaining bears,
# they would still require a shelf, so we add 1 if there's a remainder.
shelves_used = total_bears // bears_per_shelf + (total_bears % bears_per_shelf > 0)

# Print the final answer
print(f"The number of shelves used is: {shelves_used}")