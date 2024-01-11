# Dna Replication Game, Jordan Henry, v0.0

# Import Entire Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the specific tool.
from random import choice 

# Store the DNA Bases 
dnaBases = [ "A","T","G","C"]

# GAME FUNCTIONS 
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive interger number of bases to generate.\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1 
    return dnaSequence 

# dna = genDNA()
# print(dna)

def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now graduatenthe RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A fromn the DNA sequence.\n")
rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan.01,1907
rnaSequence = input("Please enter the matching RNA sequence. Leave no space Then press enter.\n").upper()
rnaStop = time.time



    return (rnaSequence,rnaTime)
    # Tuples are ORDERED -- you can reference elements with the index.
    # Tuples are UNCHANGEABLE -- you cannot add, or delete after creating
    # Tuples can have duplicate values.
