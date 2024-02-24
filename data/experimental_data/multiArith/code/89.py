# Define variables
students = 12
adults = 3
people_per_van = 5

# Calculate the total number of people going on the trip
total_people = students + adults

# Calculate the number of vans needed
# Since we can't have a fraction of a van, we use the ceiling division to round up
vans_needed = -(-total_people // people_per_van)  # This is a trick to do ceiling division with integers

# Print the final answer
print(f"Number of vans needed: {vans_needed}")