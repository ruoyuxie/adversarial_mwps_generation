# Define the initial number of eggs
total_eggs = 800

# Calculate the number of eggs that dry up (10% of total)
eggs_dry_up = total_eggs * 10 / 100

# Calculate the number of eggs that are eaten (70% of total)
eggs_eaten = total_eggs * 70 / 100

# Calculate the number of eggs remaining after drying up and being eaten
eggs_remaining = total_eggs - eggs_dry_up - eggs_eaten

# Calculate the number of eggs that hatch (1/4 of the remaining eggs)
eggs_hatch = eggs_remaining * 1 / 4

# Print the final answer
print(f"Number of frogs that hatch out of the {total_eggs} eggs: {int(eggs_hatch)}")