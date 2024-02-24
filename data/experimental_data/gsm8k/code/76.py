# Define initial variables
initial_value = 20000  # The initial value of the car in dollars
depreciation_per_year = 1000  # The annual depreciation of the car in dollars
years = 6  # The number of years after which we want to find the value of the car

# Calculate the total depreciation over the given number of years
total_depreciation = depreciation_per_year * years

# Calculate the value of the car after the given number of years
value_after_years = initial_value - total_depreciation

# Print the final answer
print("The value of the car after", years, "years is:", value_after_years)