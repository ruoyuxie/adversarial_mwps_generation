# Define the variables
total_pictures = 45
pictures_in_first_album = 27

# Calculate the number of pictures left after putting some in the first album
pictures_left = total_pictures - pictures_in_first_album

# Since the rest of the pictures are put into 9 different albums, we divide them equally
number_of_other_albums = 9
pictures_per_other_album = pictures_left // number_of_other_albums

# Print the final answer
print(f"Each of the other albums contains {pictures_per_other_album} pictures.")