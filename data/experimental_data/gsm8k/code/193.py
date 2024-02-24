# Define the initial quantity of letters needing stamps
letters_needing_stamps = 60

# Jennie stamps one-third of the letters needing stamps
stamped_by_jennie = letters_needing_stamps // 3

# Define the final quantity of already-stamped letters after Jennie's help
final_stamped_letters = 30

# Calculate the initial quantity of already-stamped letters before Jennie began
# We know that the final number of stamped letters is the sum of the initial stamped letters and the ones Jennie stamped
initial_stamped_letters = final_stamped_letters - stamped_by_jennie

# Print the final answer
print(f"The number of letters in the already-stamped pile when Jennie began was: {initial_stamped_letters}")