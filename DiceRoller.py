import random
import sys

roll = "yes"


def diceRoll():
    global rollAgain
    print("Rolling your dice...")
    print("You rolled...")
    print(str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)))
    rollAgain = input("Would you like to play again?")

def reRoll():
    rollAgain = input("Please enter a correct input. (Yes or no) : ")
    if rollAgain == "yes" or rollAgain == "y":
        diceRoll()
        reRoll()
    else:
        print("Exiting...")

if roll == "yes" or roll == "y":
    diceRoll()
    while rollAgain == "yes" or rollAgain == "y":
        diceRoll()
    else:
        if rollAgain == "no" or rollAgain == "n":
            print("Exiting...")
            sys.exit()
        else:  
          reRoll()
