#Write a program that converts 6.37 hours into hours, seconds and minutes.
#1.1 hours = 1 hour, 6 minutes
#Calcs
#.17 hours = 10.2 minutes = 612 seconds
#60 * .17 = 10.2 minutes
#.2 * 60 = 12 seconds
#
hoursEntered = float(input("Enter the number of hours to convert:"))
hoursRemainder = hoursEntered%int(hoursEntered)
remainderMinutes = 60 * hoursRemainder
remainderSeconds = remainderMinutes%int(remainderMinutes) * 60
# print("%2.2f" %hoursRemainder)
# print("%2.2f" %remainderMinutes)
# print("%2.2f" %remainderSeconds)

print(hoursEntered, "is", int(hoursEntered), "hours", int(remainderMinutes), "minutes and", int(remainderSeconds), "seconds")
