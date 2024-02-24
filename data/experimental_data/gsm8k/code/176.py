# Define the initial quantities
trees = 2
plants_per_tree = 20
seeds_per_plant = 1

# Calculate the total number of seeds collected
total_seeds = trees * plants_per_tree * seeds_per_plant

# Calculate the percentage of seeds that are planted
percentage_planted = 60

# Calculate the number of seeds planted (without using modulo operations)
seeds_planted = (total_seeds * percentage_planted) // 100

# Since each seed becomes a tree, the number of trees planted is the same as the number of seeds planted
trees_planted = seeds_planted

# Print the final answer
print(f"James planted {trees_planted} trees.")