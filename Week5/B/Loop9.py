posNum = 0
posNum = int(input("Please enter a positive number:"))
numSum = 0
numCount = 0
while (posNum >= 0):
    numSum += posNum
    posNum = int(input("Please enter a positive number (Input a negative number to quit):"))
    numCount += 1
print("The sum of all of your positive numbers is:", numSum)
print("The average of all of your positive numbers is:", numSum/numCount)
print("You entered", numCount, " positive numbers.")
