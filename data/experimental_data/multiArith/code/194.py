# Define the variables
trays_at_first_table = 10
trays_at_second_table = 2
trays_per_trip = 4

# Calculate the total number of trays
total_trays = trays_at_first_table + trays_at_second_table

# Calculate the number of full trips Roger can make
full_trips = total_trays // trays_per_trip

# Calculate if there is a need for an additional trip for the remaining trays
additional_trip = (total_trays % trays_per_trip) > 0

# Calculate the total number of trips
total_trips = full_trips + additional_trip

# Print the final answer
print(f"Roger will make {total_trips} trips to pick up all the trays.")