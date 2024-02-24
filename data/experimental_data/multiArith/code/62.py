# Define the variables
trays_per_trip = 8
trays_from_first_table = 9
trays_from_second_table = 7

# Calculate the total number of trays
total_trays = trays_from_first_table + trays_from_second_table

# Calculate the number of trips
# Since Jerry can carry 8 trays at a time, we divide the total trays by trays_per_trip
# and use the ceiling function to round up to the nearest whole number
import math
number_of_trips = math.ceil(total_trays / trays_per_trip)

# Print the final answer
print("Jerry will make", number_of_trips, "trips.")