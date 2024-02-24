# Define the initial number of bears in stock
initial_bears_in_stock = 6

# Define the number of bears in the new shipment
shipment_bears = 18

# Calculate the total number of bears after the shipment arrives
total_bears = initial_bears_in_stock + shipment_bears

# Define the number of bears per shelf
bears_per_shelf = 6

# Calculate the number of shelves used to hold all the bears
number_of_shelves = total_bears / bears_per_shelf

# Print the final answer
print(f"The number of shelves used is: {int(number_of_shelves)}")