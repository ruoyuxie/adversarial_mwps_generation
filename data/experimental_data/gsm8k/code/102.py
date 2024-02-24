# Define the total number of contestants
total_contestants = 18

# Calculate the number of female contestants
# Since a third of the contestants are female, we divide the total by 3
female_contestants = total_contestants // 3

# Calculate the number of male contestants
# The rest of the contestants are male, so we subtract the number of females from the total
male_contestants = total_contestants - female_contestants

# Print the final answer
print("Number of male contestants:", male_contestants)