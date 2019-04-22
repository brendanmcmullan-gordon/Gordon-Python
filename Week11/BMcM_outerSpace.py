import random
import time

def displayIntro():
    print("""
    You are in space. There are three planets in front of you.
    One is full of riches.
    One is deadly.
    One will trap you. 
    """)
    print()
def choosePlanet():
    planet = ''
    while planet != '1' and planet != '2' and planet != '3':
        print('Which planet will you go into? (1, 2 or 3)')
        planet = input()

    return planet

def checkPlanet(chosenPlanet):
    print('You approach the planet...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large alien jumps out in front of you! He raises his tentacles and...')
    print()
    time.sleep(2)

    friendlyPlanet = random.randint(1, 3)

#chooses a number for deadlyPlanet that isn't the one used for friendlyPlanet
    deadlyPlanet = friendlyPlanet
    while deadlyPlanet == friendlyPlanet:
        deadlyPlanet = random.randint(1, 3)

    if chosenPlanet == str(friendlyPlanet):
        print('Gives you his treasure!')
    elif chosenPlanet == str(deadlyPlanet):
        print('Slaps you back into space!')
    else:
        print('Destroys your ship and traps you!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = choosePlanet()

    checkPlanet(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
