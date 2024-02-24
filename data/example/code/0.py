# Define the initial number of ducks
total_ducks = 320

# Night 1: 1/4 of them get eaten by a fox
ducks_eaten_by_fox = total_ducks * 1/4
remaining_ducks_after_night1 = total_ducks - ducks_eaten_by_fox

# Night 2: 1/6 of the remaining ducks fly away
ducks_fly_away = remaining_ducks_after_night1 * 1/6
remaining_ducks_after_night2 = remaining_ducks_after_night1 - ducks_fly_away

# Night 3: 30 percent are stolen
ducks_stolen = remaining_ducks_after_night2 * 30/100
remaining_ducks_after_night3 = remaining_ducks_after_night2 - ducks_stolen

# Print the final number of ducks remaining
print(f"Number of ducks remaining after three nights: {int(remaining_ducks_after_night3)}")