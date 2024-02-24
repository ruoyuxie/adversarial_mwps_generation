# Define the variables
total_seats = 60000
percentage_sold = 75
fans_stayed_home = 5000

# Calculate the number of seats sold
seats_sold = (total_seats * percentage_sold) / 100

# Calculate the number of fans who attended
fans_attended = seats_sold - fans_stayed_home

# Print the final answer
print(f"The number of fans who attended the show is: {int(fans_attended)}")