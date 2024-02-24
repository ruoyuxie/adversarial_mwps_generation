# Define the quantity stored by a large cask
cask_storage = 20

# Calculate the storage capacity of a barrel, which is 3 gallons more than twice the cask's capacity
barrel_storage = 2 * cask_storage + 3

# James has 4 barrels
number_of_barrels = 4

# Calculate the total storage capacity for the barrels
total_barrel_storage = number_of_barrels * barrel_storage

# Calculate the total water storage capacity by adding the cask's storage
total_storage_capacity = total_barrel_storage + cask_storage

# Print the final answer
print("James can store a total of", total_storage_capacity, "gallons of water.")