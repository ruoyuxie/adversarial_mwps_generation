# Define the variables
pages_per_inch = 100  # Number of pages per inch when stacked
thickness_of_book_in_inches = 1.5  # Thickness of the book in inches

# Calculate the total number of pages
# Since each paper is printed on both sides, the number of pages is twice the number of papers
# The number of papers is equal to the thickness of the book times the number of pages per inch
total_number_of_papers = thickness_of_book_in_inches * pages_per_inch

# Each paper has two pages (one on each side), so we multiply by 2
total_number_of_pages = total_number_of_papers * 2

# Print the final answer
print(f"The book contains {int(total_number_of_pages)} pages.")