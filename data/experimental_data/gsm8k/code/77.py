# Define variables
charge_per_session = 18  # The charge for each session
sessions_per_month = 2   # The number of sessions each member attends per month
number_of_members = 300  # The total number of members

# Calculate the charge per member per month
charge_per_member_per_month = charge_per_session * sessions_per_month

# Calculate the total monthly income for the gym
total_monthly_income = charge_per_member_per_month * number_of_members

# Print the final answer
print("The gym makes $", total_monthly_income, " a month.", sep='')

# Alternatively, if you want to print just the number without the dollar sign and text
print(total_monthly_income)