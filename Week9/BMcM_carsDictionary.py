cars = {"Jeep":"These cars are bulky", "Porsche":"These cars are sleek", "Ford":"These cars are varied", "Volkswagen":"These cars are small"}
choice = None

while choice != "0":
    print("""
        Car Dictionary
        0 - Quit
        1 - Look up a car model
        2 - Add a car model
        3 - Redefine a description
        """)
    choice = input("Please choose an option (0, 1, 2, 3): ")

    if choice == "0":
        print("Goodbye.")

    elif choice == "1":
        carKey = input("Please enter the model of car you wish to look up: ")
        if carKey in cars:
            print(carKey, ":", cars[carKey])
            input("Press ENTER to continue.")
        else:
            print("Sorry, this model is not in the dictionary.")

    elif choice == "2":
        carKey = input("Please enter the model of car you wish to add: ")
        if carKey not in cars:
            carDesc = input("Please enter the description of the car model: ")
            cars[carKey] = carDesc
            print("The car model has been added to the dictionary.")
        else:
            print("This car model already exists in the dictionary, try redefining it.")

    elif choice == "3":
        carKey = input("Please enter the model of the car you wish to redefine: ")
        if carKey in cars:
            carDesc = input("Please enter the description of the car model: ")
            cars[carKey] = carDesc
            print("The entry for this car model has been changed.")
        else:
            print("This car model is not already in the dictionary, try adding it.")

    else:
        print("Sorry, that was an invalid choice.")
        input("Press ENTER to try again.")
