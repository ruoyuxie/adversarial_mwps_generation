# Define the growth rate variables
growth_in_4_years = 8  # inches the crocodile grows in 4 years
time_period_4_years = 4  # time period for the growth in years

# Define the target time period
target_time_period = 13  # years we want to calculate the growth for

# Calculate the growth rate per year
growth_per_year = growth_in_4_years / time_period_4_years

# Calculate the total growth over the target time period
total_growth_in_target_period = growth_per_year * target_time_period

# Print the final answer
print(f"In {target_time_period} years, the crocodile will grow {total_growth_in_target_period} inches.")

# If you want to print only the final answer without the text, you can do:
# print(total_growth_in_target_period)