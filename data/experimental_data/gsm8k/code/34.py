# Define the variables
doctor_visit_cost = 300  # Cost of the visit to the primary care doctor
insurance_coverage_percentage = 80  # Percentage of the cost covered by insurance

# Calculate the insurance coverage in dollars
insurance_coverage_dollars = (insurance_coverage_percentage / 100) * doctor_visit_cost

# Calculate James's out-of-pocket cost
james_out_of_pocket_cost = doctor_visit_cost - insurance_coverage_dollars

# Print the final answer
print("James's out-of-pocket cost is $", james_out_of_pocket_cost)