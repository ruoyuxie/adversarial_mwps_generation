# Define the number of guns each person has
dj_guns = 8
nick_guns = 10
rj_guns = 1
richard_guns = 5

# Calculate the total number of guns
total_guns = dj_guns + nick_guns + rj_guns + richard_guns

# Calculate the number of people
number_of_people = 4

# Calculate how many guns each person would have if they shared equally
guns_per_person = total_guns // number_of_people

# Since we are avoiding modulo operations, we need to ensure that the division is exact
# We can do this by subtracting the remainder from the total before dividing
remainder = total_guns - (guns_per_person * number_of_people)
total_guns -= remainder

# Recalculate guns per person after adjusting for any remainder
guns_per_person = total_guns // number_of_people

# Print the final answer
print(f"If they were to share their guns equally, each of them would have {guns_per_person} guns.")