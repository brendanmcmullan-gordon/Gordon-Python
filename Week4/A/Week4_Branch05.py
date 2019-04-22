daysMonth = int(input("Please enter the number of days in the month"))

if (daysMonth == 31):
    print("January, March, May, July, August, October and December have 31 days in the month")
else:
    if (daysMonth == 30):
        print("April, June, September and November have 30 days in the month")
    else:
        if (daysMonth == 29):
            print("February in a non-leap year has 29 days in the month")
        else:
            if (daysMonth == 28):
                print("February in a leap year has 28 days in the month")
            else:
                print("No months have", daysMonth, "days in the month")
