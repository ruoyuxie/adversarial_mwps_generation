# Define the variables
visits_per_month = 30000  # total visits in a month
earnings_per_visit = 0.01  # earnings in dollars per visit
days_per_month = 30  # number of days in a normal month

# Calculate total earnings per month
total_earnings_per_month = visits_per_month * earnings_per_visit

# Calculate earnings per day
earnings_per_day = total_earnings_per_month / days_per_month

# Print the final answer
print(f"John makes ${earnings_per_day} per day.")