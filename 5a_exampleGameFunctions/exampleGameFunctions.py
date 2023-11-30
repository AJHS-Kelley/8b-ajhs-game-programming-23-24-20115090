# Exxample Game Functions Project, Jordan Henry v10.0
import random 

# def functionOne():
#     pass 

# def functionTwo(param1):
#     pass

# def functionThree(param1 = "Default  Value"):
#     print(param1)

# def FunctionFour(param1, param2, param3):
#     pass

cars = ["corvette", "porche","ferrari","hellcat"]

print(' Lets race!')
playerSlowingDown = False

def racing(mph, playerSpeeding, playerSlowingDown, crashing):
    if mph > 100 and playerSpeeding:
        playerWinning = True
    elif mph < 100 and playerSlowingDown and crashing: 
        playerWinning = False 
    else:
        print("Catch up, your gonna get hit!\n")
        playerWinning = False 
      
    return playerWinning

racing(95.7, True, False, True) 

def carChoice(cars):
    print(cars)
    # if playerChooses (cars):
              
    #           playerWinsRace = True 
    # for i in range (len(fastestCar)):
    #         if fastestCar[i] not in cars:
    #             playerWinsRace = False 
    #             break 
    #         if playerWinsRace:
    #             print(' Congrats you have won.')
                
    #             gameIsDone = True 

    # return race

carChoice(cars)
for i in range(cars):
    print(i)
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')
#B.A.N code review by Ceon 