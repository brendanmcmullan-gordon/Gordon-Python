scoreNum = 1
totalScore = 0.0
while (scoreNum <= 5):
    testScore = float(input("Please enter a test score:"))
    totalScore += testScore
    scoreNum += 1
scoreAvg = totalScore/scoreNum
print("The average of all of the scores is %.2f" %scoreAvg )
