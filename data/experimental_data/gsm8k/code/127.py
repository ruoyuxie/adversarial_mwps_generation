# Define variables
days_in_year = 365
years = 4
writing_frequency = 2  # every other day

# Calculate the total number of days in 4 years without leap years
total_days = days_in_year * years

# Calculate the number of comics written
# Since James writes a comic every other day, we divide the total days by the writing frequency
comics_written = total_days // writing_frequency

# Print the final answer
print(f"James has written {comics_written} comics.")