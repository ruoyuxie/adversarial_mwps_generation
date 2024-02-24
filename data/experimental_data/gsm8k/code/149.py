# Define the total number of clovers in the field
total_clovers = 500

# Calculate the number of four-leaved clovers (20% of total)
four_leaved_clovers = total_clovers * 20 / 100

# Calculate the number of purple four-leaved clovers (one quarter of four-leaved clovers)
purple_four_leaved_clovers = four_leaved_clovers * 1 / 4

# Print the final answer
print(f"The number of clovers that are both purple and four-leaved is: {int(purple_four_leaved_clovers)}")