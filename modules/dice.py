# Dice rolling module by Jordan Henry, v0.0
import random 


def rollDice(numDice,sizeDice):
    numRolled = 0 
    sum = 0 
    while numRolled < numDice:
        roll = random.randint(1,sizeDice)
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1 
    return sum 