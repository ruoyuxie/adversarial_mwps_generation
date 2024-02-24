# Define the variables
bianca_recycled_pounds = 24
friends_recycled_pounds = 3
pounds_per_point = 3

# Calculate the points earned by Bianca
bianca_points = bianca_recycled_pounds / pounds_per_point

# Calculate the points earned by her friends
friends_points = friends_recycled_pounds / pounds_per_point

# Calculate the total points earned
total_points = bianca_points + friends_points

# Print the final answer
print(f"Bianca and her friends earned a total of {int(total_points)} points.")