# Define the quantities of each type of fish
number_of_bass = 32
ratio_trout_to_bass = 1 / 4
ratio_blue_gill_to_bass = 2

# Calculate the number of trout and blue gill based on the given ratios
number_of_trout = number_of_bass * ratio_trout_to_bass
number_of_blue_gill = number_of_bass * ratio_blue_gill_to_bass

# Calculate the total number of fish caught
total_fish = number_of_bass + number_of_trout + number_of_blue_gill

# Print the final answer
print(f"The fisherman caught a total of {int(total_fish)} fish.")