# Define the initial variables
total_tickets = 79
tickets_spent_dunk_clown = 23
ticket_cost_per_ride = 7

# Calculate the remaining tickets after the 'dunk a clown' booth
remaining_tickets = total_tickets - tickets_spent_dunk_clown

# Calculate the number of rides Edward can go on
number_of_rides = remaining_tickets // ticket_cost_per_ride

# Print the final answer
print("Edward can go on", number_of_rides, "rides.")