# Define initial quantities
music_files = 26
video_files = 36
total_files = music_files + video_files  # Calculate the total number of files

# Number of files deleted
files_deleted = 48

# Calculate the number of files remaining after deletion
files_remaining = total_files - files_deleted

# Print the final answer
print(f"After deleting {files_deleted} files, Amy has {files_remaining} files remaining on her flash drive.")