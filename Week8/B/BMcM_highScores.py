scores = [(55, "Tim"), (66, "John"), (56, "Fred"), (67, "Tien")]
scores.sort(reverse = True)
choice = None

while choice != "0":
    print(
        """
        High Scores 2.0
        
        0 - Quit
        1 - List Scores
        2 - Add a score       
        
        """
    )
    choice = input("Please choose 0, 1 or 2: ")

    if choice == "0":
        print("Goodbye.")
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
        input("\nPress ENTER to continue")
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:7]
    else:
        print("Sorry, invalid choice.")
        input("Press ENTER to choose again.")
input("Press ENTER to exit.")
