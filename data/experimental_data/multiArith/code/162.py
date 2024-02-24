# Define initial variables based on the problem statement
initial_tickets = 4  # Tickets Jerry won initially
tickets_spent = 2    # Tickets Jerry spent on a beanie
additional_winnings = 47  # Tickets Jerry won later

# Calculate the remaining tickets after spending on the beanie
remaining_tickets_after_spending = initial_tickets - tickets_spent

# Calculate the total tickets Jerry has after winning more tickets
total_tickets = remaining_tickets_after_spending + additional_winnings

# Print the final answer
print(f"Jerry has {total_tickets} tickets.")