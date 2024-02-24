# Define the variables
red_marbles = 38
total_marbles = 63

# Calculate the number of green marbles (half as many as red ones)
green_marbles = red_marbles // 2

# Calculate the number of dark blue marbles
# Total marbles is the sum of red, green, and dark blue marbles
dark_blue_marbles = total_marbles - (red_marbles + green_marbles)

# Print the final answer
print("Number of dark blue marbles:", dark_blue_marbles)