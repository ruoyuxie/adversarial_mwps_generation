# Define variables based on the problem statement
price_per_deck = 9  # dollars
initial_decks = 12  # number of decks the magician started with
decks_left = 7      # number of decks left at the end of the day

# Calculate the number of decks sold
decks_sold = initial_decks - decks_left

# Calculate the total earnings from the decks sold
total_earnings = decks_sold * price_per_deck

# Print the final answer
print("The magician earned", total_earnings, "dollars.")