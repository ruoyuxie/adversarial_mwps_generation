# Define the initial number of coloring books
initial_coloring_books = 120

# Define the number of coloring books sold
coloring_books_sold = 39

# Calculate the number of coloring books left after the sale
coloring_books_left = initial_coloring_books - coloring_books_sold

# Define the number of coloring books per shelf
books_per_shelf = 9

# Calculate the number of shelves used to hold the remaining coloring books
shelves_used = coloring_books_left // books_per_shelf

# Print the final answer
print("The number of shelves used is:", shelves_used)