# Define the variables
total_votes = 80  # Total number of students who voted
winner_fraction = 3/4  # Fraction of votes the winner got

# Calculate the number of votes the winner got
winner_votes = total_votes * winner_fraction

# Since the total votes are the sum of the winner's and loser's votes,
# we can find the loser's votes by subtracting the winner's votes from the total votes.
loser_votes = total_votes - winner_votes

# Print the final answer
print(f"The number of votes the loser got is: {int(loser_votes)}")