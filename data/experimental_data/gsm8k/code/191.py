# Define the variables
number_of_shelters = 6
people_per_shelter = 30
cans_per_person = 10

# Calculate the total number of people serviced by all shelters
total_people_serviced = number_of_shelters * people_per_shelter

# Calculate the total number of cans of soup Mark donates
total_cans_donated = total_people_serviced * cans_per_person

# Print the final answer
print("Mark donates", total_cans_donated, "cans of soup.")