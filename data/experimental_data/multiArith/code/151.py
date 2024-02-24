# Define the variables
total_pictures = 65
pictures_in_first_album = 17
number_of_other_albums = 6

# Calculate the number of pictures remaining after the first album
remaining_pictures = total_pictures - pictures_in_first_album

# Calculate the number of pictures in each of the other albums
pictures_per_other_album = remaining_pictures // number_of_other_albums

# Print the final answer
print(f"The number of pictures in each of the other albums is: {pictures_per_other_album}")