# Define the variables
total_time_for_8_visits = 20  # Total time in minutes for 8 bathroom visits
number_of_visits_done = 8     # Number of bathroom visits already done
number_of_visits_needed = 6   # Number of bathroom visits we want to calculate the time for

# Calculate the time per visit
time_per_visit = total_time_for_8_visits / number_of_visits_done

# Calculate the total time for the desired number of visits
total_time_for_6_visits = time_per_visit * number_of_visits_needed

# Print the final answer
print(f"It would take {total_time_for_6_visits} minutes for John to go to the bathroom 6 times.")