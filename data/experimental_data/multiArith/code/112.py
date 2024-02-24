# Define variables
points_per_bag = 5  # points earned for each bag of cans recycled
total_bags = 11     # total number of bags Wendy had
unrecycled_bags = 2 # number of bags Wendy didn't recycle

# Calculate the number of bags actually recycled
recycled_bags = total_bags - unrecycled_bags

# Calculate the total points earned
total_points = points_per_bag * recycled_bags

# Print the final answer
print("Wendy would have earned", total_points, "points.")