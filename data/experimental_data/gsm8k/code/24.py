# Define the variables
steps_per_minute = 2000 / 30  # Roger's walking speed in steps per minute
daily_goal = 10000  # Roger's daily step goal

# Calculate the time needed to reach the daily goal
# Since we know the steps per minute, we can find the total minutes by dividing the daily goal by steps per minute
minutes_to_reach_goal = daily_goal / steps_per_minute

# Print the final answer
print(f"It will take Roger {minutes_to_reach_goal} minutes to reach his goal of {daily_goal} steps.")