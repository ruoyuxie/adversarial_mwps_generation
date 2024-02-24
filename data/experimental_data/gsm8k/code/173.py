# Define variables
flowers_planted_per_day = 2
total_days = 15
flowers_that_did_not_grow = 5

# Calculate the total number of flowers planted
total_flowers_planted = flowers_planted_per_day * total_days

# Calculate the number of flowers that grew successfully
flowers_that_grew = total_flowers_planted - flowers_that_did_not_grow

# Print the final answer
print("Ryan has", flowers_that_grew, "flowers in his garden after 15 days.")