# Define the variables
total_windows_needed = 12
windows_already_installed = 6
installation_time_per_window = 4  # in hours

# Calculate the number of windows left to install
windows_left_to_install = total_windows_needed - windows_already_installed

# Calculate the total installation time for the remaining windows
total_installation_time = windows_left_to_install * installation_time_per_window

# Print the final answer
print(f"The builder will take {total_installation_time} hours to install the rest of the windows.")