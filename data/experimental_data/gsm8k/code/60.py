# Define the initial quantity of tennis balls
total_tennis_balls = 100

# James gives away half of the tennis balls
tennis_balls_given_away = total_tennis_balls // 2

# The remaining half is to be put into containers
tennis_balls_remaining = total_tennis_balls - tennis_balls_given_away

# There are 5 large containers to fill with the remaining tennis balls
number_of_containers = 5

# Calculate how many tennis balls go into each container
tennis_balls_per_container = tennis_balls_remaining // number_of_containers

# Print the final answer
print(f"Each container will hold {tennis_balls_per_container} tennis balls.")