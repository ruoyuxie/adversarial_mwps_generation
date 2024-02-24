# Define the initial variables
total_seeds = 41
seeds_planted_in_big_garden = 29
seeds_per_small_garden = 4

# Calculate the remaining seeds after planting in the big garden
remaining_seeds = total_seeds - seeds_planted_in_big_garden

# Calculate the number of small gardens by dividing the remaining seeds by the number of seeds per small garden
number_of_small_gardens = remaining_seeds // seeds_per_small_garden

# Print the final answer
print("Emily had", number_of_small_gardens, "small gardens.")