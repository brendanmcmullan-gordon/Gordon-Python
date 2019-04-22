userName = input("Please enter your name:")
userAge = int(input("Please enter your age:"))

repControl = 1
numReps = int(input("Please enter the number of times you wish this to repeat:"))

while (repControl <= numReps):
    print(repControl, ". Your name is ", userName, " and you are ", userAge, " years old.", sep="")
    repControl += 1

