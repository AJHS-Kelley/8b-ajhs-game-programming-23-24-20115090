# Select the secret number from a given range.
# Player must guess the number. 
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    #Tell them the number of guesses left. 
    # Tell them if too high/ too low. 
# What happens if guess is right?
    # Tell them guess is correct.
    # Award a point. 
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU. 
# Check to see if player or CPU has >= points, if so they win.

import random # Import the random module to our code.

# DECLARATIONS
secretnumber = -1
playerGuess =-1 
playerScore = 0 
cpuScore = 0 
numGuesses = 0 
playerName = "" 
difficulty = ""
rangeMin = -1
rangeMax = -1
numAttempts = 5
NewSecretNumber = 25 
difficulty = ""

print(""" 
     
      
      
      """)


# CPU SECRET NUMBER GENERATION 

secretNumber = random.randint(0, 20)
print(secretNumber)

# GAME LOOP
print( "You need to guess a number from 0 to 20 and you have four guesses.\nIf you guess it right get point. If you  guess it wrong you try again.") 
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH MATCH.
# print() an explanation of your three difficulty levels.
# Use input() to store difficulty in difficulty variable
# assign values to numAttempts, rangeMin, and rangeMax based on choice 

difficulty = " choose your difficulty "
playerName = input("What should I call you?\n")
print(f"Hello {playerName}, how are you?")
if difficulty == "easy":
 numAttempts = 5
rangeMin = -1
rangeMax = -1 

if difficulty == "medium":
    numAttempts = 3
    rangeMin =  -1
    rangeMax = -1 

if difficulty == "hard":
   numAttempts = 2
   rangeMin = 0
   rangeMax = 0 

if difficulty == "extremely hard":
   numAttempts = 1
   rangeMin = 0 
   rangeMax = 0 

while playerScore != 3 and cpuScore !=3: # START THE MATCH (GAME)
    # Diffculty code needs to be BEFORE the round starts.
    # pass -- Tells pyhtons to skip this block of code 
    print (f"Player Score: {playerScore}\nCPU Score: {cpuScore}. \n")
    secretNumber = random.randint(0, 20)
# Whenever you assign a specific value to something, its called " hard coded".
#print(secretNumber)
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND. 


    



    numGuesses= 0 
    for guesses in range(4):
        print(f"You have {4-numGuesses} guesses remaining.\n")
        playerGuess = (input("Type a number from 0 to 20 and press ENTER.\n"))
        # input() saves all  data as a STRING by default.
        # int() will convert to an INTEGER
        # float() will convert to FLOAT
        print(f"You have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("Whoa dude, what a guess! You got it!\n")
            playerScore +=1 
            break # IMMEADIATELY EXIT ANY LOOP YOU ARE IN!
        else:
            print("You did not guess correctly.\n")
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else: 
                print("Your guess is too low.\n") 
        numGuesses += 1 
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")
if playerScore >= 3:
    print("Winner, winner, chicken dinner! You scored 3 points first\n") 
else: 
    print("Yo, you  lost to a computer. You are a scrub.\n")
