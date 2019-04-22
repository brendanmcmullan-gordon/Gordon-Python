intFour = 0
intFour = int(input("Please enter a number between 1 and 4 inclusive:"))
while (intFour < 1 or intFour > 4):
    intFour = int(input("Please enter a correct number."))
print("You entered", intFour)
if (intFour == 1):
    print("You entered 'one'.")
elif (intFour == 2):
    print("You entered 'two'.")
elif (intFour == 3):
    print("You entered 'three'.")
elif (intFour == 4):
    print("You entered 'four'.")
