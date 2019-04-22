posNum = 0
posNum = int(input("Please enter a positive number:"))
numSum = 0
while (posNum != 0):
    numSum += posNum
    posNum = int(input("Please enter a positive number (Enter 0 to quit):"))
print("The sum of all of your numbers is:", numSum)
