# Define initial variables
initial_subscribers = 150  # James's initial number of subscribers
gifted_subscribers = 50    # Number of subscribers gifted to James
subscription_fee = 9       # Amount James earns per subscriber per month

# Calculate the total number of subscribers after the gift
total_subscribers = initial_subscribers + gifted_subscribers

# Calculate the total monthly earnings
monthly_earnings = total_subscribers * subscription_fee

# Print the final answer
print("James makes $", monthly_earnings, " a month from his Twitch subscribers.", sep='')

# Alternatively, if you want to print just the number as the answer:
print(monthly_earnings)