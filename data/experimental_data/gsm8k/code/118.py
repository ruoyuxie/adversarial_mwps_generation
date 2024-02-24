# Define the variables based on the given problem
distance_traveled = 1200  # in miles
time_taken = 3  # in hours

# Calculate the rate of the plane
rate_of_plane = distance_traveled / time_taken  # in miles per hour

# Define the additional distance to be traveled
additional_distance = 2000  # in miles

# Calculate the additional time needed to travel the additional distance
# at the same rate
additional_time_needed = additional_distance / rate_of_plane  # in hours

# Print the final answer
print(f"At the same rate, it would take an additional {additional_time_needed} hours to travel {additional_distance} miles.")

# If you want to print just the number of hours as an integer
print(int(additional_time_needed))