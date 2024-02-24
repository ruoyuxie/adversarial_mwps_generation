# Define the total number of pages in the book
total_pages = 600

# Coral reads half of the book in the first week
pages_read_first_week = total_pages / 2

# Calculate the remaining pages after the first week
remaining_pages_after_first_week = total_pages - pages_read_first_week

# Coral reads 30 percent of the remaining pages the second week
percent_read_second_week = 0.30
pages_read_second_week = remaining_pages_after_first_week * percent_read_second_week

# Calculate the remaining pages after the second week
remaining_pages_after_second_week = remaining_pages_after_first_week - pages_read_second_week

# The number of pages Coral must read the third week to finish the book
pages_to_read_third_week = remaining_pages_after_second_week

# Print the final answer
print(f"Coral must read {int(pages_to_read_third_week)} pages the third week to finish the book.")