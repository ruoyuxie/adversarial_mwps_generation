# Define the variable for the coconut flavored jelly beans
coconut_flavored_jelly_beans = 750

# According to the problem, 1/4 of the red jelly beans are coconut flavored
# Let's denote the total number of red jelly beans as red_jelly_beans
# Therefore, coconut_flavored_jelly_beans = 1/4 * red_jelly_beans
# We can find the total number of red jelly beans by multiplying by 4
red_jelly_beans = coconut_flavored_jelly_beans * 4

# The problem states that 3/4 of the jelly beans are red
# Let's denote the total number of jelly beans in the jar as total_jelly_beans
# Therefore, red_jelly_beans = 3/4 * total_jelly_beans
# We can find the total number of jelly beans by dividing by 3 and then multiplying by 4
total_jelly_beans = (red_jelly_beans / 3) * 4

# Print the final answer
print(f"The total number of jelly beans in the jar is: {int(total_jelly_beans)}")