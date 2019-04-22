startingBalance = float(input("Please enter your bank balance."))
interestRate = 0.0
interestEarned = 0.0
finalBalance = 0.0

if (startingBalance < 1000.00 ):
    interestRate = 0.05
else:
    if (startingBalance >= 1000.00 and startingBalance < 10000.00):
        interestRate = 0.055
    else:
#        if (startingBalance >= 10000.00)
            interestRate = 0.06

interestEarned = startingBalance*interestRate
finalBalance = startingBalance+interestEarned

print("Your starting balance is $%.2f" %startingBalance)
print("Your interest rate is", interestRate*100, "percent")
print("The amount of interest you've earned is $%.2f" %interestEarned)
print("Your final balance is $%.2f" %finalBalance)
#print(startingBalance, interestRate, interestEarned, finalBalance)
