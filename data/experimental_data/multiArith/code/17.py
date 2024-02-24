# Define the quantities mentioned in the problem
red_apples_ordered = 6
green_apples_ordered = 15
students_wanting_fruit = 5

# Each student who wants fruit gets 1 apple, so we subtract that number from the total ordered
total_apples_ordered = red_apples_ordered + green_apples_ordered
apples_given_to_students = students_wanting_fruit

# Calculate the number of extra apples the cafeteria ended up with
extra_apples = total_apples_ordered - apples_given_to_students

# Print the final answer
print(f"The cafeteria ended up with {extra_apples} extra apples.")