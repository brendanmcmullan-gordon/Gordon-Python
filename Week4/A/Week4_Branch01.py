hoursMinutes = float(input("Please input the time in hh.mm format"))
if (hoursMinutes > 24.00):
    print("Please enter a valid time")

else:

    if (hoursMinutes > 12.00):
        print("It is after noon")

    else:
        print("It is before noon")
