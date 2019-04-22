lightOn = ""
electricityOn = ""
globeBlown = ""
fuseBlown = ""

lightOn = input("Is the light on? Yes/No:")
if (lightOn == "Yes"):
    print("Good, all is OK")
elif (lightOn == "No"):
    electricityOn = input("Is the electricity turned off? Yes/No:")
    if (electricityOn == "Yes"):
        print("Turn on the electricity at the switch.")
    elif (electricityOn == "No"):
        globeBlown = input("Has the light globe blown? Yes/No:")
        if (globeBlown == "Yes"):
            print("Replace the light globe.")
        elif (globeBlown == "No"):
            fuseBlown = input("Has the fuse blown? Yes/No:")
            if (fuseBlown == "Yes"):
                print("Replace the fuse.")
            elif (fuseBlown == "No"):
                print("Call an electrician.")
print("Thank you for using Trouble Shooter.")
