# Define the initial variables
total_candy = 108
candy_eaten = 36
candy_per_pile = 9

# Calculate the remaining candy after Sarah ate some
remaining_candy = total_candy - candy_eaten

# Calculate the number of piles Sarah can make with the remaining candy
number_of_piles = remaining_candy // candy_per_pile

# Print the final answer
print(f"Sarah can make {number_of_piles} piles of candy.")