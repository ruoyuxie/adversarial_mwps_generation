# Define the initial variables
total_candy = 32
candy_eaten = 12
candy_per_pile = 5

# Calculate the remaining candy after Bianca ate some
remaining_candy = total_candy - candy_eaten

# Calculate the number of piles Bianca can make with the remaining candy
number_of_piles = remaining_candy // candy_per_pile

# Print the final answer
print(f"Bianca can make {number_of_piles} piles of candy.")