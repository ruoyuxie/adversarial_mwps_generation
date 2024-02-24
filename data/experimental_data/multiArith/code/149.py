# Define variables based on the problem statement
price_per_deck = 7  # dollars per magic card deck
initial_decks = 16  # number of decks the magician started with
remaining_decks = 8  # number of decks left at the end of the day

# Calculate the number of decks sold
decks_sold = initial_decks - remaining_decks

# Calculate the total earnings from the decks sold
total_earnings = decks_sold * price_per_deck

# Print the final answer
print("The magician earned", total_earnings, "dollars.")