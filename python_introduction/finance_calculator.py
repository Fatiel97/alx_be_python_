# Define the variables
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))                                

# Calculate Monthly Savings:
Monthly_Savings = monthly_income - monthly_expenses

# Project Annual Savings:
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

print(f"Your monthly savings are ${Monthly_Savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings:.2f}")
