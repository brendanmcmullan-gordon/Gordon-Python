numFiftys = int(input("How many fifty cent coins do you have?"))
numTwentys = int(input("How many twenty cent coins do you have?"))

moneyInFiftys = numFiftys*.5
moneyInTwentys = numTwentys*.2

totalMoney = moneyInFiftys+moneyInTwentys
print("You have $%.2f" %moneyInFiftys, "in fifty cent coins and $%.2f" %moneyInTwentys, "in twenty cent coins.")
print("You have $%.2f" %totalMoney, "in total.")
