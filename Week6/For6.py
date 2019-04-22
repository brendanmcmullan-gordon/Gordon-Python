testScore = 0.0
scoreTotal = 0.0
scoreCount = 0
scoreAvg = 0.0
num = 0

for num in range(5):
    testScore = float(input("Please enter a test score:"))
    scoreCount +=1
    scoreTotal += testScore
print("The average test score is", scoreTotal/scoreCount)
