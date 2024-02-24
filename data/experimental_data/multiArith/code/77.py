# Define the variables
total_pictures = 33
pictures_in_first_album = 27

# Calculate the remaining pictures after putting some in the first album
remaining_pictures = total_pictures - pictures_in_first_album

# Since the remaining pictures are distributed evenly in 3 different albums,
# we divide the remaining pictures by 3 to find out how many are in each of the other albums
pictures_in_each_of_the_other_albums = remaining_pictures // 3

# Print the final answer
print(f"The number of pictures in each of the other three albums is: {pictures_in_each_of_the_other_albums}")