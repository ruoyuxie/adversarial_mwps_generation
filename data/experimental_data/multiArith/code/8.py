# Define the quantities mentioned in the problem
red_apples = 42
green_apples = 7
students_wanting_fruit = 9

# Each student who wants fruit gets 1 apple, so we assume they all take 1 red apple first
# Calculate the number of red apples taken by students
red_apples_taken = min(students_wanting_fruit, red_apples)

# Calculate the remaining red apples after the students have taken theirs
remaining_red_apples = red_apples - red_apples_taken

# If there are still students wanting fruit after all red apples are taken, they will take green apples
# Calculate the number of students still wanting fruit after taking red apples
students_still_wanting_fruit = max(students_wanting_fruit - red_apples_taken, 0)

# Calculate the number of green apples taken by the remaining students
green_apples_taken = min(students_still_wanting_fruit, green_apples)

# Calculate the remaining green apples after the students have taken theirs
remaining_green_apples = green_apples - green_apples_taken

# Calculate the total number of extra apples the cafeteria ended up with
extra_apples = remaining_red_apples + remaining_green_apples

# Print the final answer
print(f"The cafeteria ended up with {extra_apples} extra apples.")