# Define the variables
speed_mph = 60  # Jace's driving speed in miles per hour
first_drive_hours = 4  # Duration of the first driving period in hours
break_hours = 0.5  # Duration of the break in hours (30 minutes is 0.5 hours)
second_drive_hours = 9  # Duration of the second driving period in hours

# Calculate the distance traveled during the first driving period
first_distance = speed_mph * first_drive_hours

# Calculate the distance traveled during the second driving period
second_distance = speed_mph * second_drive_hours

# Calculate the total distance traveled
total_distance = first_distance + second_distance

# Print the final answer
print(f"Jace will travel {total_distance} miles.")