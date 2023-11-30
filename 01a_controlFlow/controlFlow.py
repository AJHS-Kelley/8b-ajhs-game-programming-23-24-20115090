# Control Flow, Jordan Henry v0.0
# DECLARATIONS 

favColor = "green"
luckyNumber = 7 
myGPA = 3.5
myAge = 17 
pineappleOnPizza = False

# # if statenents - checking for a certain condition to be true or fasle, do something if true
# if favColor == "blue":
#     print("i like cheeseburgers")

# if myGPA == 3.5:
#     print("that  person is tall)")

# # if-else statement -- Check for a condition, do something for 
# if myGPA >= 3.0:
#     print("Congratulations on making honor roll!")
# else:
#     print("Better luck next year. Try to study more!")
# if myAge >= 16:
#     print("Happy sweet sixteeth!")
# else :    print(" almost there!") 

# # if- elif -else statements -- Checks for multiple conditions
# if myAge > 19:
#     print("Almost there") 
# elif myAge > 16:
#     print (" your getting there!")
# else:
#     print(" your not growing")
# # 1 if, 1 else, any of elif allowed. 

# # Nested if - elif -else Statements 
# if myAge > 15:
#     print("Congratulations you are elgible for a liscense") 
# elif  myGPA > 2.0:
#     print(" you qualify for $500 of a car")
# else:
#     print( " yo0u get nothing ")
# else:
#     print(" you are not old enough to drive") 

# when doing if -elif statements, check for the highest value first  

# while loop -- Think " MUSICAL CHAIRS" -- Used when you do Not know how many iterations you need. 
# iteration = one complete trip through a loop 
x = 0 
while x < 100:
    print(f"X is currently equal to {x}")
    x += 1 

while x >= 100:
    print(f"X is currently equal to {x}")
    x -= 1

# for loop -- Think ' Go Fish' , used when you know number of iterations needed.
print("FOR LOOP STARTS HERE")
for i in range (10): # i = iterable variable 
    print(i)

print("EVEN OR ODD LOOP!") 
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That  number is even!")
    else :
        print("That number is odd!")


# () Parenthesis 
# []  Sqaure Brackets 
# <> Angle Brackets 
# {} Braces 