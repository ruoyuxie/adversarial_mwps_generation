# Define the variables based on the given problem
# Let's denote the number of joggers Tyson bought as 'tyson_joggers'

# Christopher bought twenty times as many joggers as Tyson
# Christopher bought 80 joggers
christopher_joggers = 80
multiplier_to_tyson = 20
tyson_joggers = christopher_joggers // multiplier_to_tyson

# Alexander bought 22 more joggers than Tyson
additional_joggers_alexander = 22
alexander_joggers = tyson_joggers + additional_joggers_alexander

# Calculate how many more joggers Christopher bought than Alexander
more_joggers_christopher_than_alexander = christopher_joggers - alexander_joggers

# Print the final answer
print(f"Christopher bought {more_joggers_christopher_than_alexander} more joggers than Alexander.")