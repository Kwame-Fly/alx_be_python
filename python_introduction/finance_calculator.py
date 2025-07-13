#Finance calculator
#Prompt user to enter monthly income
monthly_income = int (input("Enter your monthly income:"))
#Prompt user to enter monthly expenses
monthly_expenses = int (input("Enter your total monthly expenses:"))
#Calculate monthly savings by deducting expenses from income
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
#Assume projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)
#Output of results
print (f"Your monthly savings are ${monthly_savings}.")
print (f"Projected savings after one year, with interest, is: ${projected_savings}.")