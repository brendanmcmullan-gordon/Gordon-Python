itemPrice = None
totalCost = 0.0
payMethod = ""
cashGiven = 0.0
cashChange = 0.0

custName = input("Please enter your name: ")
print()

while itemPrice != 0:
    print("=====Enter 0 to finish=====")
    itemPrice = input("Please enter the price of your item (dd.cc): $")
    try:
        itemPrice = float(itemPrice)
        totalCost += itemPrice
    except ValueError:
        continue

print("Your total is: $%.2f" %totalCost)
print()
payMethod = input("Please enter your method of payment (Cash or Credit): ")
payMethod = payMethod.lower()

if payMethod == "credit":
    if totalCost < 20.00:
        print("Attention: This payment is less than $20.00 and will be processed as a cash payment.")
        payMethod = "cash"
    else:
        print("Processing your payment ...")
        print("Your payment has been processed! Thanks for shopping at BRUNNINGS, ", custName, "!", sep="")
        exit()

if payMethod == "cash":
    cashGiven = float(input("Please enter the amount of cash given for payment: $"))
    cashChange = cashGiven - totalCost
    print("Your change is $%.2f" %cashChange, sep="")
    print("Thanks for shopping at BRUNNINGS, ", custName, "!", sep="")
    exit()
