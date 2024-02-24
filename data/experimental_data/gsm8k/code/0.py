# Define the variables
pam_bags = 10
gerald_bags_per_pam_bag = 3
apples_per_gerald_bag = 40

# Calculate the number of apples in one of Pam's bags
apples_in_one_pam_bag = gerald_bags_per_pam_bag * apples_per_gerald_bag

# Calculate the total number of apples Pam has
total_apples_pam_has = pam_bags * apples_in_one_pam_bag

# Print the final answer
print(f"Pam has a total of {total_apples_pam_has} apples.")