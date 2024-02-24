# Define initial variables
initial_elevation = 400  # John's starting elevation in feet
descent_rate = 10        # John's descent rate in feet per minute
time_traveled = 5        # Time John travels downward in minutes

# Calculate the total descent
total_descent = descent_rate * time_traveled

# Calculate John's final elevation
final_elevation = initial_elevation - total_descent

# Print the final answer
print("John's elevation now is:", final_elevation)