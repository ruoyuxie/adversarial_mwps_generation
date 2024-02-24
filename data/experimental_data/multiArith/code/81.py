# Define the variables
total_problems = 40
completed_problems = 26
remaining_pages = 2

# Calculate the number of problems left
problems_left = total_problems - completed_problems

# Calculate the number of problems per page
problems_per_page = problems_left // remaining_pages

# Print the final answer
print(f"The number of problems on each page is: {problems_per_page}")