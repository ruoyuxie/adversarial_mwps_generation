# Define the initial variables
total_strawberries = 300  # Total number of strawberries Cheryl placed
total_buckets = 5         # Total number of buckets
strawberries_removed_per_bucket = 20  # Number of strawberries Cheryl decided to take out from each bucket

# Calculate the number of strawberries in each bucket before removing any
strawberries_per_bucket_initial = total_strawberries / total_buckets

# Calculate the number of strawberries left in each bucket after removing some
strawberries_per_bucket_final = strawberries_per_bucket_initial - strawberries_removed_per_bucket

# Print the final answer
print(f"Number of strawberries left in each bucket: {strawberries_per_bucket_final}")