# Define the variables for the number of girls and boys trying out
number_of_girls = 30
number_of_boys = 36

# Define the variable for the number of students who got called back
students_called_back = 10

# Calculate the total number of students who tried out
total_students_tried_out = number_of_girls + number_of_boys

# Calculate the number of students who didn't make the cut
students_didnt_make_cut = total_students_tried_out - students_called_back

# Print the final answer
print("Number of students who didn't make the cut:", students_didnt_make_cut)