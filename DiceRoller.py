import random
import sys

Response = input("Would you like to roll the dice?: ").lower() 



def Roll():
    Dice = random.randint(1,6)
    print(Dice)
    return Dice
    
    
    
def RollAgain():  
    Reply = input("Would you like to roll again?: ").lower()
    if Reply == "yes":
        Dice = Roll()
    elif Reply == "no":
        sys.exit()
    
  
if Response == "yes":
    Roll()
    while Response == "yes":
        RollAgain()
elif Response == "no":
    sys.exit()
    

