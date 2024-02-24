# Define the variable for Darcie's age
darcie_age = 4

# Darcie is 1/6 as old as her mother, so we can define her mother's age
# Let's call her mother's age 'mother_age'
# darcie_age = 1/6 * mother_age
# To find mother_age, we multiply Darcie's age by 6
mother_age = darcie_age * 6

# Her mother is 4/5 as old as her father, so we can define her father's age
# Let's call her father's age 'father_age'
# mother_age = 4/5 * father_age
# To find father_age, we divide mother_age by 4 and then multiply by 5
father_age = (mother_age / 4) * 5

# Print the final answer
print("Darcie's father is", int(father_age), "years old.")