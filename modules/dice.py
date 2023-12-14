# Dice rolling module by Jordan Henry, v0.0
import random 


def roll(numDice,sizeDice):
    numRolled = 0 
    sum = 0 
    while numRolled < numDice:
        roll = random.randint(1,sizeDice)
        sum += roll
        numRolled += 1 
    return sum  


def display(numDice,sizeDice):
    numRolled = 0 
    sum = 0 
    while numRolled < numDice:
        roll = random.randint(1,sizeDice)
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1 
    return sum 

def isDoubles(roll1,roll2):
    if roll1 == roll2:
        isDoubles = True 
    else: 
        isDoubles = False 
        return isDoubles 

def isExploding(roll, sizeRoll):
    if roll == sizeRoll:
        isExploding = True 
    else :
        isExploding = False
    return isExploding