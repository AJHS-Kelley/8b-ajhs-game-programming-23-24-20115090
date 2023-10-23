# FUNCTION -- a named piece oof code that can be reused easily.
# FUNCTION SIGNATURE -- syntax for creating a new function 
def exampleFunctionA(): # NO PARAMETERS 
    count = 0
    num = int(input("How many times do you want to wish a happy birthday?\n"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1

def exampleFunction(num, count): # PARAMETERS
    while count < num:
        print("Happy Birthday!\n")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION!
exampleFunctionA()
exampleFunctionB(5,0)
