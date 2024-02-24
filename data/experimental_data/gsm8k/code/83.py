# Define the total distance of the road trip
total_distance = 1000

# Let's denote the distance driven by Katie as 'katie_distance'.
# According to the problem, Michelle drives 3 times the distance Katie drives.
# So, Michelle's distance is 'michelle_distance = 3 * katie_distance'.

# Tracy drives 20 miles more than twice Michelle's distance.
# So, Tracy's distance is 'tracy_distance = 2 * michelle_distance + 20'.

# The sum of all distances driven by Tracy, Michelle, and Katie equals the total distance.
# Therefore, tracy_distance + michelle_distance + katie_distance = total_distance.

# Now, let's express everything in terms of 'katie_distance' and solve for it.
# (2 * (3 * katie_distance) + 20) + (3 * katie_distance) + katie_distance = total_distance
# Simplify the equation:
# 6 * katie_distance + 20 + 3 * katie_distance + katie_distance = total_distance
# 10 * katie_distance + 20 = total_distance
# 10 * katie_distance = total_distance - 20

# Now, solve for 'katie_distance':
katie_distance = (total_distance - 20) / 10

# Now that we have Katie's distance, we can find Michelle's distance:
michelle_distance = 3 * katie_distance

# Print the final answer
print(f"Michelle drives {michelle_distance} miles.")

# Let's verify the calculation by checking if the sum of all distances equals the total distance
tracy_distance = 2 * michelle_distance + 20
total_calculated_distance = tracy_distance + michelle_distance + katie_distance
assert total_calculated_distance == total_distance, "The distances do not add up correctly."

# If the assertion passes, the calculation is correct.