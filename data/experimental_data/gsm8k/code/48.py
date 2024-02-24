# Define the maximum reward for the ProcGen environment
procgen_max_reward = 240

# Calculate the maximum reward for the CoinRun environment, which is half of ProcGen's maximum reward
coinrun_max_reward = procgen_max_reward / 2

# Greg's PPO algorithm obtained 90% of the possible reward on the CoinRun environment
# Calculate the percentage as a decimal
percentage_obtained = 90 / 100

# Calculate the actual reward Greg's PPO algorithm got
gregs_reward = coinrun_max_reward * percentage_obtained

# Print the final answer
print(f"Greg's PPO algorithm got a reward of: {gregs_reward}")