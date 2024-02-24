# Define variables for the quantities mentioned in the problem
correct_answers_first_half = 8
correct_answers_second_half = 2
points_per_question = 8

# Calculate the score for the first half
score_first_half = correct_answers_first_half * points_per_question

# Calculate the score for the second half
score_second_half = correct_answers_second_half * points_per_question

# Calculate the final score by adding both halves
final_score = score_first_half + score_second_half

# Print the final answer
print("Adam's final score is:", final_score)