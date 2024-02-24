# Define the initial variables
total_candy = 78
candy_eaten = 30
candy_per_pile = 8

# Calculate the remaining candy after Bianca ate some
remaining_candy = total_candy - candy_eaten

# Calculate the number of piles Bianca can make with the remaining candy
number_of_piles = remaining_candy // candy_per_pile

# Print the final answer
print("Bianca can make", number_of_piles, "piles of candy.")