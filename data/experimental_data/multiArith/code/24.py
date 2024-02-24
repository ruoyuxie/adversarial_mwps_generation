# Define the variables
total_problems = 101
completed_problems = 47
remaining_pages = 6

# Calculate the number of problems left
problems_left = total_problems - completed_problems

# Calculate the number of problems per page
problems_per_page = problems_left // remaining_pages

# Print the final answer
print("There are", problems_per_page, "problems on each page.")