# Define the initial number of files
initial_files = 85

# Define the number of files deleted
deleted_files = 40

# Calculate the remaining files after deletion
remaining_files = initial_files - deleted_files

# Define the number of files per folder
files_per_folder = 5

# Calculate the number of folders needed for the remaining files
number_of_folders = remaining_files // files_per_folder

# Print the final answer
print("Katie ended up with", number_of_folders, "folders.")