viewMonths = input("Do you wish to view the months? Yes/No:")


if (viewMonths == "Yes"):
    viewAllMonths = input("Do you wish to view all of the months? Yes/No:")
    if (viewAllMonths == "Yes"):
        print("January, February, March, April, May, June, July, August, September, October, November, December")
    elif (viewAllMonths == "No"):
        viewLongMonths = input("Do you wish to view months with 31 days? Yes/No:")
        if (viewLongMonths == "Yes"):
                print("January, March, May, July, August, October and December have 31 days in the month")
        elif (viewLongMonths == "No"):
                print("April, June, September and November have 30 days in the month")
elif (viewMonths == "No"):
    viewWeekend = input("Do you wish to view week end days? Yes/No:")
    if (viewWeekend == "Yes"):
        print("Saturday and Sunday are weekend days")
    elif (viewWeekend == "No"):
        print("Monday, Tuesday, Wednesday, Thursday and Friday are weekdays")
