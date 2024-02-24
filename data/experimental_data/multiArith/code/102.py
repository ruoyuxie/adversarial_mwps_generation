# Define the variables
total_flowers_picked = 53
flowers_per_bouquet = 7
wilted_flowers = 18

# Calculate the number of flowers left after some wilted
flowers_left = total_flowers_picked - wilted_flowers

# Calculate the number of bouquets Paige can make with the remaining flowers
bouquets_possible = flowers_left // flowers_per_bouquet

# Print the final answer
print("Paige can still make", bouquets_possible, "bouquets for her friend's wedding.")