# Define the initial variables
total_pages = 120
percentage_used_for_science = 25  # in percent
pages_used_for_math = 10

# Calculate the number of pages used for the science project
pages_used_for_science = (percentage_used_for_science / 100) * total_pages

# Calculate the total number of pages used
total_pages_used = pages_used_for_science + pages_used_for_math

# Calculate the number of pages remaining
pages_remaining = total_pages - total_pages_used

# Print the final answer
print(f"Pages remaining in the pad: {int(pages_remaining)}")