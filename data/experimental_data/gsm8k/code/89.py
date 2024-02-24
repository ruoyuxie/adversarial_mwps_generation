# Define the total number of fish caught
total_fish = 36

# Define the number of fish Carla caught
carla_fish = 8

# Calculate the number of fish caught by Kyle and Tasha together
kyle_tasha_fish = total_fish - carla_fish

# Since Kyle and Tasha caught the same number of fish, we divide by 2 to find the number each caught
kyle_fish = kyle_tasha_fish // 2

# Print the final answer
print(f"Kyle caught {kyle_fish} fish.")