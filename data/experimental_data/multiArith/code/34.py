# Define the variables
total_windows_needed = 10
windows_already_installed = 6
time_per_window = 5  # hours

# Calculate the number of windows left to install
windows_left_to_install = total_windows_needed - windows_already_installed

# Calculate the total time to install the remaining windows
total_time_to_install_remaining = windows_left_to_install * time_per_window

# Print the final answer
print("The builder will take", total_time_to_install_remaining, "hours to install the remaining windows.")