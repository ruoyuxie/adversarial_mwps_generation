# Define variables based on the problem statement
hives = 5
honey_per_hive_liters = 20
jar_capacity_liters = 0.5

# Calculate total honey produced
total_honey_liters = hives * honey_per_hive_liters

# Since the friend is bringing jars for half the honey, James needs jars for the remaining half
honey_for_james_liters = total_honey_liters / 2

# Calculate the number of jars James needs
jars_needed = honey_for_james_liters / jar_capacity_liters

# Print the final answer
print(f"James needs to buy {int(jars_needed)} jars.")