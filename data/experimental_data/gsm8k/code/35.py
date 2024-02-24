# Define the initial quantity of sheets of paper
total_sheets_of_paper = 2450

# Define the number of binders the sheets are split into
number_of_binders = 5

# Calculate the number of sheets of paper per binder
sheets_per_binder = total_sheets_of_paper // number_of_binders

# Justine takes a binder and colors on one-half of the sheets
sheets_colored_by_justine = sheets_per_binder // 2

# Print the final answer
print(f"Justine used {sheets_colored_by_justine} sheets of paper.")