# Define the variables
total_problems = 60
finished_problems = 20
remaining_pages = 5

# Calculate the number of problems left
problems_left = total_problems - finished_problems

# Calculate the number of problems per page
problems_per_page = problems_left / remaining_pages

# Print the final answer
print(f"The number of problems on each page is: {problems_per_page}")