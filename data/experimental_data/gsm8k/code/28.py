# Define the variables
sprints_per_day = 3  # Number of sprints James runs each time
days_per_week = 3    # Number of times per week James runs
meters_per_sprint = 60  # Distance in meters for each sprint

# Calculate the total distance run in one day
total_meters_per_day = sprints_per_day * meters_per_sprint

# Calculate the total distance run in a week
total_meters_per_week = total_meters_per_day * days_per_week

# Print the final answer
print("James runs a total of", total_meters_per_week, "meters in a week.")