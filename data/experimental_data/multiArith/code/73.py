# Define variables
total_friends_invited = 9
friends_who_couldnt_come = 6
cupcakes_per_person = 2

# Calculate the number of friends who can come
friends_coming = total_friends_invited - friends_who_couldnt_come

# Including Sam, calculate the total number of people at the party
total_people_at_party = friends_coming + 1  # +1 for Sam

# Calculate the total number of cupcakes needed
total_cupcakes_needed = total_people_at_party * cupcakes_per_person

# Print the final answer
print("Sam should buy", total_cupcakes_needed, "cupcakes.")