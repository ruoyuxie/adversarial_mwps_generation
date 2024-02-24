# Define the variables for the quantities mentioned in the problem
vanessa_recycled_pounds = 20
friends_recycled_pounds = 16
pounds_per_point = 9

# Calculate the points earned by Vanessa and her friends
vanessa_points = vanessa_recycled_pounds // pounds_per_point
friends_points = friends_recycled_pounds // pounds_per_point

# Calculate the total points earned
total_points = vanessa_points + friends_points

# Print the final answer
print("Total points earned:", total_points)