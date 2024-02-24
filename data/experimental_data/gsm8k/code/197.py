# Define variables corresponding to the quantities mentioned in the problem
memory_card_capacity_mb = 3000 * 8  # Total capacity in megabytes
picture_size_mb_old = 8             # Old picture size in megabytes
picture_size_mb_new = 6             # New picture size in megabytes

# Calculate the total number of pictures with the old size
total_pictures_old = memory_card_capacity_mb / picture_size_mb_old

# Calculate the total number of pictures with the new size
total_pictures_new = memory_card_capacity_mb / picture_size_mb_new

# Print the final answer
print(f"The memory card can hold {int(total_pictures_new)} pictures of {picture_size_mb_new} megabytes each.")