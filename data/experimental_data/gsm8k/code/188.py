# Define the number of rooms in Danielle's apartment
danielle_rooms = 6

# Calculate the number of rooms in Heidi's apartment
# Heidi's apartment has 3 times as many rooms as Danielle's
heidi_rooms = danielle_rooms * 3

# Calculate the number of rooms in Grant's apartment
# Grant's apartment has 1/9 as many rooms as Heidi's
grant_rooms = heidi_rooms * (1/9)

# Since the number of rooms should be an integer, we round down to the nearest whole number
grant_rooms = int(grant_rooms)

# Print the final answer
print(f"Grant's apartment has {grant_rooms} rooms.")