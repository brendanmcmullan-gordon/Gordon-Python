netFaults = {"No Connection": "Check your network cables for disconnections", "High Latency": "Check that your network isn't saturated", "Slow Speed":"Check that your network isn't saturated", "Spotty Connection":"Check that your cables are plugged in properly", "No External Connection":"Check that your default gateway is set properly", "Network Collision":"Check that your IP Address is not the same as another device"}
choice = None

while choice != "0":
    print("""
        Network Faults Dictionary
        0 - Quit
        1 - Look up a Network Fault
        2 - Add a Network Fault
        3 - Redefine a Network Fault
        4 - Delete a Network Fault
        5 - Print the list of faults in the dictionary
        """)
    choice = input("Please choose an option (0, 1, 2, 3, 4, 5): ")

    if choice == "0":
        print("Goodbye.")

    elif choice == "1":
        faultKey = input("Please enter the network fault you wish to look up: ")
        if faultKey in netFaults:
            print(faultKey, ":", netFaults[faultKey])
            input("Press ENTER to continue.")
        else:
            print("Sorry, this network fault is not in the dictionary.")

    elif choice == "2":
        faultKey = input("Please enter the network fault you wish to add: ")
        if faultKey not in netFaults:
            faultDesc = input("Please enter the fix for the network fault: ")
            netFaults[faultKey] = faultDesc
            print("The network fault has been added to the dictionary.")
            input("Press ENTER to continue.")
        else:
            print("This network fault already exists in the dictionary, try redefining it.")

    elif choice == "3":
        faultKey = input("Please enter the network fault you wish to redefine: ")
        if faultKey in netFaults:
            faultDesc = input("Please enter the fix for the network fault: ")
            netFaults[faultKey] = faultDesc
            print("The entry for this network fault has been changed.")
            input("Press ENTER to continue.")
        else:
            print("This network fault is not already in the dictionary, try adding it.")

    elif choice == "4":
        faultKey = input("Please enter the network fault you wish to delete: ")
        if faultKey in netFaults:
            del netFaults[faultKey]
            print("The network fault has been deleted.")
            input("Press ENTER to continue.")
        else:
            print("This network fault is not in the dictionary")

    elif choice == "5":
        print(netFaults.keys())
        input("Press ENTER to continue")
    else:
        print("Sorry, that was an invalid choice.")
        input("Press ENTER to try again.")
