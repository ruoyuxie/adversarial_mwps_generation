# Define the variables
trays_at_first_table = 17
trays_at_second_table = 55
trays_per_trip = 9

# Calculate the total number of trays
total_trays = trays_at_first_table + trays_at_second_table

# Calculate the number of full trips Dave can make
full_trips = total_trays // trays_per_trip

# Calculate if there is a need for an additional trip for the remaining trays
additional_trip = (total_trays % trays_per_trip) > 0

# Calculate the total number of trips
total_trips = full_trips + additional_trip

# Print the final answer
print(f"Dave will make {total_trips} trips.")