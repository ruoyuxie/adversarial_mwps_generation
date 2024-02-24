# Define the variables
number_of_packs = 10
cards_per_pack = 20
uncommon_card_ratio = 1/4

# Calculate the total number of cards
total_cards = number_of_packs * cards_per_pack

# Calculate the number of uncommon cards per pack
uncommon_cards_per_pack = cards_per_pack * uncommon_card_ratio

# Calculate the total number of uncommon cards
total_uncommon_cards = number_of_packs * uncommon_cards_per_pack

# Print the final answer
print(f"John got {int(total_uncommon_cards)} uncommon cards.")