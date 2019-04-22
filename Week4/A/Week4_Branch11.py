grossIncome = float(input("Please enter your gross annual income in dollars:"))
taxDeduct = float(input("Please enter your tax deductions in dollars:"))
taxableIncome = 0.0
taxRate = 0.0
taxPayable = 0.0
netIncome = 0.0

if (grossIncome >= 0.0 and grossIncome < 18200.00 ):
    taxRate = 0.0
else:
    if (grossIncome >= 18200.00 and grossIncome < 37000.00 ):
        taxRate = 0.19
    else:
        if (grossIncome >= 37000.00 and grossIncome < 90000.00 ):
            taxRate = 0.325
        else:
            if (grossIncome >= 90000.00 and grossIncome < 180000.00 ):
                taxRate = 0.37
            else:
                if (grossIncome >= 180000.00):
                    taxRate = 0.45

taxableIncome = grossIncome-taxDeduct
taxPayable = taxableIncome*taxRate
netIncome = grossIncome-taxPayable

print("Your gross income is $%.2f" %grossIncome)
print("Your tax deductions are $%.2f" %taxDeduct)
print("Your tax rate is", taxRate*100, "percent")
print("The amount of tax you owe is $%.2f" %taxPayable)
print("Your net income is $%.2f" %netIncome)
