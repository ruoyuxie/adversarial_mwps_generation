# Define the variables
time_between_bathroom_visits = 50  # time in minutes
movie_duration = 2.5 * 60  # convert 2.5 hours to minutes

# Calculate the number of times John uses the bathroom
# Initialize the counter for bathroom visits
bathroom_visits = 0

# Initialize the time tracker
time_passed = 0

# Loop through the movie duration in increments of time_between_bathroom_visits
while time_passed < movie_duration:
    # Increment the time tracker by the time between bathroom visits
    time_passed += time_between_bathroom_visits
    
    # Check if the time passed is still within the movie duration
    if time_passed <= movie_duration:
        # Increment the bathroom visit counter
        bathroom_visits += 1

# Print the final answer
print(f"John uses the bathroom {bathroom_visits} times during a 2.5-hour movie.")