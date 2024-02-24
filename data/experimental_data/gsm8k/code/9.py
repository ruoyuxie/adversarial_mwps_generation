# Define the variables
notebooks = 5
pages_per_notebook = 40
pages_per_day = 4

# Calculate the total number of pages
total_pages = notebooks * pages_per_notebook

# Calculate the number of days the notebooks will last
days_last = total_pages // pages_per_day

# Print the final answer
print("The notebooks will last for", days_last, "days.")