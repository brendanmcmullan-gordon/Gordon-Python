fiftyNum = 0
numSum = 0
numCount = 0
while (numSum <= 100):
    fiftyNum = int(input("Please enter a number between 1 & 50:"))
    if(fiftyNum < 1 or fiftyNum > 50):
        print("You have entered a number out of the range, try again:")
    else:
        numSum += fiftyNum
        numCount += 1
        print("Sum is:", numSum)
print("The sum of all of your numbers is:", numSum)
print("You entered", numCount, "numbers.")
print("The average of all of your numbers is:", numSum/numCount)
