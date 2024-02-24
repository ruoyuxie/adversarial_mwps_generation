# Define the variables
cards_added_by_sasha = 48
fraction_taken_by_karen = 1/6

# Calculate the number of cards taken out by Karen
cards_taken_by_karen = cards_added_by_sasha * fraction_taken_by_karen

# Calculate the number of cards left after Karen took out some
cards_left_after_karen = cards_added_by_sasha - cards_taken_by_karen

# Given that there are now 83 cards in the box
total_cards_after_karen = 83

# Calculate the original number of cards in the box
original_cards_in_box = total_cards_after_karen - cards_left_after_karen

# Print the final answer
print(f"The original number of cards in the box was: {original_cards_in_box}")