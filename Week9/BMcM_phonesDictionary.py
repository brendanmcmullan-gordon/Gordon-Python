phones = {"Apple": "These phones are expensive", "Nokia": "These phones are indestructible"}
choice = None

while choice != "0":
    print("""
        Phone Dictionary
        0 - Quit
        1 - Look up a phone model
        2 - Add a phone model
        3 - Redefine a description
        4 - Delete a phone model
        """)
    choice = input("Please choose an option (0, 1, 2, 3, 4): ")

    if choice == "0":
        print("Goodbye.")

    elif choice == "1":
        phoneKey = input("Please enter the model of phone you wish to look up: ")
        if phoneKey in phones:
            print(phoneKey, ":", phones[phoneKey])
            input("Press ENTER to continue.")
        else:
            print("Sorry, this model is not in the dictionary.")

    elif choice == "2":
        phoneKey = input("Please enter the model of phone you wish to add: ")
        if phoneKey not in phones:
            phoneDesc = input("Please enter the description of the phone model: ")
            phones[phoneKey] = phoneDesc
            print("The phone model has been added to the dictionary.")
        else:
            print("This phone model already exists in the dictionary, try redefining it.")

    elif choice == "3":
        phoneKey = input("Please enter the model of the phone you wish to redefine: ")
        if phoneKey in phones:
            phoneDesc = input("Please enter the description of the phone model: ")
            phones[phoneKey] = phoneDesc
            print("The entry for this phone model has been changed.")
        else:
            print("This phone model is not already in the dictionary, try adding it.")

    elif choice == "4":
        phoneKey = input("Please enter the model of phone you wish to delete: ")
        if phoneKey in phones:
            del phones[phoneKey]
            print("The phone model has been deleted.")
        else:
            print("This model of phone is not in the dictionary")

    else:
        print("Sorry, that was an invalid choice.")
        input("Press ENTER to try again.")
