# Define variables for the quantities mentioned in the problem
questions_correct_first_half = 3
questions_correct_second_half = 2
points_per_question = 3

# Calculate the score for the first half
score_first_half = questions_correct_first_half * points_per_question

# Calculate the score for the second half
score_second_half = questions_correct_second_half * points_per_question

# Calculate the final score by adding both halves
final_score = score_first_half + score_second_half

# Print the final answer
print("Frank's final score is:", final_score)