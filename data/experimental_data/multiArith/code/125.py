# Define variables
points_per_bag = 8  # points earned for each bag of cans recycled
total_bags = 14     # total number of bags Megan had
unrecycled_bags = 5 # number of bags Megan didn't recycle

# Calculate the number of bags actually recycled
recycled_bags = total_bags - unrecycled_bags

# Calculate the total points earned
total_points = points_per_bag * recycled_bags

# Print the final answer
print("Megan would have earned", total_points, "points.")