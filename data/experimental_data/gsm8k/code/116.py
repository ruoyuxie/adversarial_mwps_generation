# Define the variables
hourly_rate = 12  # Weng's hourly rate in dollars
babysitting_time_minutes = 50  # Time spent babysitting in minutes

# Convert babysitting time from minutes to hours
babysitting_time_hours = babysitting_time_minutes / 60

# Calculate the earnings
earnings = hourly_rate * babysitting_time_hours

# Since we want the answer without using modulo operations and without fractions,
# we can round down the earnings to the nearest whole number.
# This is equivalent to truncating the decimal part of the earnings.
earnings_whole_dollars = int(earnings)

# Print the final answer
print("Weng earned $", earnings_whole_dollars, sep='')

# Alternatively, if you want to ensure that the script does not use any form of rounding
# and strictly performs a step-by-step calculation that would be done by hand, you can
# calculate the earnings by multiplying the hourly rate by the fraction of the hour worked.

# Calculate the fraction of the hour worked
fraction_of_hour_worked = babysitting_time_minutes / 60

# Calculate the earnings by multiplying the hourly rate by the fraction of the hour worked
earnings_exact = hourly_rate * fraction_of_hour_worked

# Since we know that 50 minutes is 5/6 of an hour, the exact calculation would be:
# earnings_exact = 12 * (5/6)
# earnings_exact = 12 * 5 / 6
# earnings_exact = 60 / 6
# earnings_exact = 10

# Print the exact earnings without any rounding
print("Exact earnings: $", earnings_exact, sep='')