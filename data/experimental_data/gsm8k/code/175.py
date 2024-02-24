# Define the variables
sneezing_duration_minutes = 2  # John's sneezing fit duration in minutes
sneeze_interval_seconds = 3    # Interval between sneezes in seconds

# Convert sneezing duration to seconds
sneezing_duration_seconds = sneezing_duration_minutes * 60

# Calculate the number of sneezes
# Since John sneezes once every 3 seconds, we divide the total duration by the interval
number_of_sneezes = sneezing_duration_seconds // sneeze_interval_seconds

# Print the final answer
print(f"John sneezes {number_of_sneezes} times during his sneezing fit.")