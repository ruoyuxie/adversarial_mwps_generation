# Define the initial variables
total_candy = 54
candy_eaten = 33
candy_per_pile = 7

# Calculate the remaining candy after Emily ate some
remaining_candy = total_candy - candy_eaten

# Calculate the number of piles she can make with the remaining candy
number_of_piles = remaining_candy // candy_per_pile

# Print the final answer
print("Emily can make", number_of_piles, "piles of candy.")