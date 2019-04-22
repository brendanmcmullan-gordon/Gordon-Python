yardWidth = float(input("Input the width of the yard in metres."))
yardLength = float(input("Input the length of the yard in metres."))
houseWidth = float(input("Input the width of the house in metres."))
houseLength = float(input("Input the length of the house in metres."))


yardArea = yardWidth*yardLength
houseArea = houseWidth*houseLength
grassArea = yardArea-houseArea

print("")
print("The area of the yard is", yardArea, "sq metres")
print("The area of the house is", houseArea, "sq metres")
print("There is", grassArea, "sq metres of grass")

cuttingTimeSeconds = grassArea/.2
#print(cuttingTimeSeconds)
cuttingTimeMinutes = int(cuttingTimeSeconds/60)
#print(cuttingTimeMinutes)
cuttingTimeSecondsRemainder = cuttingTimeSeconds - cuttingTimeMinutes*60
#print(cuttingTimeSecondsRemainder)
print("")
print("It would take", int(cuttingTimeSeconds), "seconds, or", cuttingTimeMinutes, "minute(s) and", int(cuttingTimeSecondsRemainder), "seconds to cut the grass at 0.2 sq metres per second")
