# Define initial variables
initial_books_in_bin = 4
books_sold = 3
books_added = 10

# Calculate the number of books after selling some
books_after_sale = initial_books_in_bin - books_sold

# Calculate the final number of books after adding more
final_books_in_bin = books_after_sale + books_added

# Print the final answer
print(f"The final number of books in the bin is: {final_books_in_bin}")