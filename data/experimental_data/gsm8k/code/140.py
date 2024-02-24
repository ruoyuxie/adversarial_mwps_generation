# Define the variables based on the given problem
total_distance_initial = 270  # miles
total_time_initial = 3  # hours

# Calculate the rate of the train
train_speed = total_distance_initial / total_time_initial  # miles per hour

# Define the additional distance to be traveled
additional_distance = 180  # miles

# Calculate the additional time needed to travel the additional distance
# using the same rate
additional_time = additional_distance / train_speed  # hours

# Print the final answer
print(f"The additional hours needed to travel {additional_distance} miles is: {additional_time}")