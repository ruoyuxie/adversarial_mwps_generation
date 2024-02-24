# Define the variables
words_per_minute = 90
words_per_page = 450
number_of_pages = 10

# Calculate the total number of words Tom needs to type
total_words_to_type = words_per_page * number_of_pages

# Calculate the time it will take to type out the total number of words
time_to_type_one_word = 1 / words_per_minute
total_time_minutes = time_to_type_one_word * total_words_to_type

# Print the final answer
print(f"It would take Tom {total_time_minutes} minutes to type out {number_of_pages} pages.")

# If you want to print just the number as the answer, you can do the following:
print(total_time_minutes)