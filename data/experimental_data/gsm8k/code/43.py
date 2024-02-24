# Define the initial variables
annual_salary = 40000  # Steve's annual salary in dollars
tax_rate = 0.20        # 20 percent tax rate
healthcare_rate = 0.10 # 10 percent healthcare rate
union_dues = 800       # Local union dues in dollars

# Calculate the amount lost to taxes
taxes = annual_salary * tax_rate

# Calculate the amount lost to healthcare
healthcare = annual_salary * healthcare_rate

# Calculate the total deductions
total_deductions = taxes + healthcare + union_dues

# Calculate the take-home salary
take_home_salary = annual_salary - total_deductions

# Print the final answer
print(f"Steve takes home ${take_home_salary} after all deductions.")