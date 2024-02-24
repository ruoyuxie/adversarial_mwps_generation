# Define the variables
total_flowers_picked = 66
flowers_per_bouquet = 8
wilted_flowers = 10

# Calculate the number of flowers left after some wilted
flowers_left = total_flowers_picked - wilted_flowers

# Calculate the number of bouquets Isabel can make
number_of_bouquets = flowers_left // flowers_per_bouquet

# Print the final answer
print("Isabel can still make", number_of_bouquets, "bouquets for her friend's wedding.")