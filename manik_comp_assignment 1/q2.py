#program to compute income tax
 
#  taking input
Gross_Income=int(input("Enter your gross income in dollars: "))
No_of_dependents=int(input("Enter total dependents: "))
 
#  standard values
Standard_deduction=10000
Dependent_deduction=3000
Tax_Rate=0.20
 
# calculation
Taxable_income = Gross_Income - Standard_deduction - Dependent_deduction*No_of_dependents
Tax = Taxable_income * Tax_Rate
if Tax<0:
    Tax=0
 
 
#   printing output
print("Your income tax is: ", Tax) 