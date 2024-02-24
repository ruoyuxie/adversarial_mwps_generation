# Define initial quantities
mike_books_tuesday = 45
corey_books_tuesday = 2 * mike_books_tuesday  # Corey has twice as many books as Mike

# Define the number of books given away on Wednesday
mike_books_given = 10
corey_books_given = mike_books_given + 15  # Corey gives 15 more books than Mike

# Calculate the total number of books Lily received
lily_books_received = mike_books_given + corey_books_given

# Print the final answer
print("Lily received a total of", lily_books_received, "books.")