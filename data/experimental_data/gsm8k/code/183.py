# Define the total cost of the car
total_cost = 2100

# Define the number of days in a week
days_in_week = 7

# Define the number of days Sue's sister will use the car
sister_days = 4

# Calculate the number of days Sue will use the car
sue_days = days_in_week - sister_days

# Calculate the percentage of the week Sue will use the car
sue_percentage = sue_days / days_in_week

# Calculate the amount Sue has to pay based on her percentage of use
sue_payment = total_cost * sue_percentage

# Print the final answer
print(f"Sue has to pay: ${sue_payment:.2f}")