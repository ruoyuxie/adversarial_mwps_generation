# Define the variables based on the quantities mentioned in the problem
tickets_from_whack_a_mole = 26
tickets_from_skee_ball = 19
ticket_cost_per_candy = 9

# Calculate the total number of tickets Ned won
total_tickets = tickets_from_whack_a_mole + tickets_from_skee_ball

# Calculate how many candies Ned can buy
number_of_candies = total_tickets // ticket_cost_per_candy

# Print the final answer
print("Ned can buy", number_of_candies, "candies.")