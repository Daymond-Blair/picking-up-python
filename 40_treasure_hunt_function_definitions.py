# 40 41 Treasure Hunt Game - function skeleton (definitions) - docstring (multi-line comment)

import time
import random


# use the keyword "pass" in the body of  definitions
def displayGameIntro():

    print('''

                ------> Welcome to the 'Python Treasure Hunt Game' <------
                After a long journey, you find yourself in front of two caves.
                One cave leads to treasure, the other, a bottomless pit of lava.
                Summoning your courage, you decide to choose a cave!
                ''')


def chooseCave():
    cave = ' '

    while cave != '1' and cave != '2':

        print("So which cave are you going to explore? (1 or 2)")
        cave = input()
        if cave == '0':
            print("\nYou don't see the two caves right in front of you? C'mon!\n")
        elif cave < '0':
            print("\nNegative caves? What are you a time traveler? PICK A CAVE!\n")
        elif cave != '1' and cave != '2':
            print("\nUmmm I said there's only two caves!\n")
        else:
            break
    return cave


def enterCave(caveChoice):
    print("\n Looks like we're in he cave now. Everything is fine! \n")
    time.sleep(1)

    random_cave = random.randint(1, 2)
#print("random_cave = " + str(random_cave))
    if random_cave == int(caveChoice):
        print("-----> Hey it looks like you lived! I think I see the chest!")
    else:
        print("-------> Oh no; it was a Mimic!!!")


def main():
    ''' main() function controls the flow of the game by calling functions and using conditionals '''

    playGameAgain = "yes"

    while playGameAgain == "yes" or playGameAgain == "y":

        displayGameIntro()
        caveChoice = chooseCave()
        enterCave(caveChoice)

        print("\n\nDo you want to try again? (yes or no)")
        playGameAgain = input()
        print("You said: " + playGameAgain)
        time.sleep(1)

        if playGameAgain == "yes" or playGameAgain == "y":
            print("\nLet's try again!")

        else:
            print("\nOk, well later bud!")

    '''chooseCave()
    caveChoice = chooseCave()
    print("Ahhh cave number " + caveChoice + "; good luck with that!")'''


# run program
main()
