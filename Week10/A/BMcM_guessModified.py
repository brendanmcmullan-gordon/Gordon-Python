

import random
choice = None
def ask_number():
    userName = input("Please enter your name:")
    print("\nWelcome to 'Guess my number',", userName)
    print("I'm thinking of a number between 1 & 20")

    theNumber = random.randint(1,10)
    tries = 0

    while tries <= 6:
        guess = int(input("Try to guess it - take a guess: "))
        tries = tries + 1
        if guess > theNumber :
            print("Lower...")
        if guess < theNumber :
            print("Higher..")
        if guess == theNumber:
            break

    if guess == theNumber:
        tries = str(tries)
        print("You guessed it,", userName, ". The number was", theNumber)
        print("and you only took",tries,"tries")

    if guess != theNumber:
        print("No, the number I was thinking of was",theNumber)

while choice != "0":
    choice = input("""
    Would you like to play the guess the number game?
    0 - Exit
    1 - Play
    """)
    if choice == "1":
        ask_number()
input("\n Press any key to exit")
