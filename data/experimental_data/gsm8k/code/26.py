# Define the initial variables
total_credit = 100  # Total credit allowed
payment_1 = 15      # Payment made on Tuesday
payment_2 = 23      # Payment made on Thursday

# Calculate the remaining credit to be paid
# by subtracting the payments from the total credit
remaining_credit = total_credit - (payment_1 + payment_2)

# Print the final answer
print(f"Mary will need to pay ${remaining_credit} before her next shopping trip.")