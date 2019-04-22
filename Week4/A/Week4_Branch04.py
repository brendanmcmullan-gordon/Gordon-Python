day = input("Please enter a day of the week in Proper Case")

if (day == "Sunday" or day == "Saturday"):
    print(day, "falls on the weekend")
else:
    if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"):
        print(day, "is a weekday")
