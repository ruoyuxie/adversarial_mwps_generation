# Define the total amount of money to be divided
total_money = 100

# Define the ratio of Jeff's share to Brad's share
jeff_to_brad_ratio = 4

# Since Jeff gets 4 times as much as Brad, we can represent the shares as:
# Jeff's share = 4 * Brad's share

# Let's denote Brad's share as 'x'. Then Jeff's share is '4x'.
# The sum of their shares is the total money:
# x + 4x = total_money

# Solve for x (Brad's share)
# 5x = total_money
brad_share = total_money / (1 + jeff_to_brad_ratio)

# Calculate Jeff's share
jeff_share = jeff_to_brad_ratio * brad_share

# Print the final answer
print(f"Jeff gets {jeff_share} dollars.")