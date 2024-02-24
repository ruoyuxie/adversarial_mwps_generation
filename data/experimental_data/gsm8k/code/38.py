# Define the parts for each component of the drink
parts_coke = 2
parts_sprite = 1
parts_mountain_dew = 3

# Given quantity of Coke
ounces_coke = 6

# Calculate the total parts of the drink
total_parts = parts_coke + parts_sprite + parts_mountain_dew

# Calculate the size of one part based on the amount of Coke
# Since 2 parts are Coke and we have 6 ounces of Coke, each part is 6 ounces / 2 parts
size_of_one_part = ounces_coke / parts_coke

# Calculate the total ounces of the drink by multiplying the size of one part by the total parts
total_ounces = size_of_one_part * total_parts

# Print the final answer
print(f"The total ounces of the drink is: {total_ounces}")