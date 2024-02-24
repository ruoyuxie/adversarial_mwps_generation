# Define the variables for the quantities mentioned in the problem
pictures_from_phone = 2
pictures_from_camera = 4

# Calculate the total number of pictures uploaded
total_pictures = pictures_from_phone + pictures_from_camera

# Define the number of albums
number_of_albums = 3

# Calculate the number of pictures in each album
# Since the problem states that each album has the same amount of pictures,
# we divide the total number of pictures by the number of albums
pictures_per_album = total_pictures // number_of_albums

# Print the final answer
print(f"The number of pictures in each album is: {pictures_per_album}")