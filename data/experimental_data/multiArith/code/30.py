# Define the variables for the quantities mentioned in the problem
haley_recycled_pounds = 11
friends_recycled_pounds = 16
pounds_per_point = 3

# Calculate the points earned by Haley
haley_points = haley_recycled_pounds // pounds_per_point

# Calculate the points earned by her friends
friends_points = friends_recycled_pounds // pounds_per_point

# Calculate the total points earned
total_points = haley_points + friends_points

# Print the final answer
print("Total points earned:", total_points)