# Define the variables
monthly_income = input\s*\(\s*['\"]Enter your monthly income:\s*['\"]\s*\)
total_monthly_expenses = float(input("Enter your total monthly expenses :"))                                

# Calculate Monthly Savings:
monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))

# Project Annual Savings:
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

print(f"the user’s monthly savings is  {Monthly_Savings}")
print(f"the projected annual savings after including interest is  {Projected_Savings}")
