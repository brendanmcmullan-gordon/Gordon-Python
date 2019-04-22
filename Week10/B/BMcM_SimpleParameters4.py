def calculateInterest(principal, interestRate):
    print("Principal: $", principal, sep="")
    print("Interest Rate: %", interestRate*100, sep="")
    print("Interest Earned: $", principal*interestRate, sep="")
    print("")

def investForOneYear(oldPrincipal, interestRate):
    interestEarned = oldPrincipal*interestRate
    displayInterest = interestRate*100
    print("Starting Principal: $", oldPrincipal, sep="")
    print("Interest Rate: %", "%.2f" % displayInterest, sep="")
    print("Interest Earned: $%.2f" %interestEarned, sep="")
    print("New Principal: $", oldPrincipal+interestEarned, sep="")
    print("")


calculateInterest(10000, 0.06)
investForOneYear(100000, 0.076)
