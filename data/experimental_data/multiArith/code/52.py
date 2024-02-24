# Define the quantities mentioned in the problem
red_apples = 25
green_apples = 17
students_who_want_fruit = 10

# Assume each student will take only one fruit
total_fruits_ordered = red_apples + green_apples

# Calculate the number of extra fruits the cafeteria ended up with
extra_fruits = total_fruits_ordered - students_who_want_fruit

# Print the final answer
print(f"The cafeteria ended up with {extra_fruits} extra fruits.")