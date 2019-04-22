# This is the simple guess the number game.
# Remember to take care with indenting
import random
#Intial statements to the user
userName = input("Please enter your name:")
print("\nWelcome to 'Guess my number',", userName)
print("I'm thinking of a number between 1 & 20")
#set initial values
theNumber = random.randint(1,10)
tries = 0
#guessing loop
while tries <= 6:
    guess = int(input("Try to guess it - take a guess: "))
# add one to number of tries each time through the loop
# very important step, (without it, you set up an infinite loop.)
    tries = tries + 1
    if guess > theNumber :
        print("Lower...")
    if guess < theNumber :
        print("Higher..")
    if guess == theNumber:
        break
# back outside the loop
if guess == theNumber:
    tries = str(tries)
    print("You guessed it,", userName, ". The number was", theNumber)
    print("and you only took",tries,"tries")

if guess != theNumber:
    print("No, the number I was thinking of was",theNumber)

input("\n Press any key to exit")
