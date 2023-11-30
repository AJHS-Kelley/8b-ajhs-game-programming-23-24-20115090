# Hangman game by Jordan Henry , v0.0
# CRT:  You have at least one error preventing your code from executing.  Please see my comments
# and fix the code ASAP. 
import = random # remove the = sign on this line. 
words = 'cat dog hat pat rat saw sad bed tab pet school uniform microsoft program operate function collection instructions license hangman ironic nauseous coincidental phenomenom onomatopoeia necessary appealing seperate platonic electrons'.split()

# VARIABLE_NAMES in all CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
    =======''','''
    +---+
     O  |
        |
        |
    =======''','''
    +---+
     O  |
     |  |
        |
    =======''','''
    +---+
     O  |
    /|  |
        |
    =======''','''
    +---+
     O  |
    /|\ |
        |
    =======''','''
    +---+
     O  |
    /|\ |
     /\ |
    =======''']

# PICK WORD FROM LIST
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0,len(wordList)-1)
    # len(listname) -1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()
    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print() 

# i = 0 
# while i < 100:
#     word = getRandomWord()
#     print(word)
#     i += 1

    blanks = '_' * len(secretword) 

    # Replace Blanks with correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = '')
        print()

def getGuess(alreadyGuesed):
    while True:
        print('Please guess a letter then press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcedfghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English alaphabet.')
        else:
            return guess 
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game
print(' Lets play Hangman!')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False 

# Main Game Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check To see if Winner, Winner Chicken Dinner
        foundAllLetters = True 
        for i in range (len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False 
                break 
            if foundAllLetters:
                print(' Congrats you have won.')
                print('The secret word was'+ secretWord)
                gameIsDone = True 
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('You have mae this number of correct guesse' + str(len(correctLetters)))
            print('The secret word was'+ secretWord)
            gameIsDone = True 

    if gameIsDone:
        if playAgain():
        missedLetters = ''
        correctLetters = ''
        gameIsDone = False 
        secretWord = getRandomWord(words)
    else:
        break









 


