#Data Types and Operators, Jordan Henry, v0.6
# Variable Rules 
# CANNOT START WITH A NUMBER !!!!!!!!!!!
# CANNOT USE BUILT IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED.
# snake_case variables use_ to seperate words, all lower case.
# camelCase variables do not use spaces , 1st word lower, rest upper.

# String Literal Examples 
playername = "spiderman"
emptyString = ""
spaceString = " "
cookieCounter= "15 cookies"

# Integer Data Types 
# health = 100
# extralives = 5 
# temperature = -17 

# Floating Point Data Types
# pi= 3.1415678
# laptime = 3.8 
#velocity = -2.0  
# speed = 5.0

# Boolean Data Types 
isFireType = False
weaponEquipped = True 
pypEnabled = False 

# Arithmetic Operators 
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print (7+-10) # Addition 
print (5-3) # Subtraction
print (2*3) #Multiplication
print ( 10/2) # Division
print (3**6) # exponents 
print (7%8) # Modulus -- Divides, then returns remainder, most commonly used to determine even/odd
 
 # Comparison operators 
 # Evaluate the expression then return True or False 
 print(4 > 2) # Greater than
 print(9 >= 8 ) # Greater than or equal to 
 print(3 < 5) # Less than 
 print (8 <= 10) # Less than or equal to 
 print (7 == 7) # is equal to 
 print (-3 != 3) # is not equal to 

# Assignment Operators 
myVariable = "myValue" # Assign variable on left the value on the right, throw out any current value
myOthervariable = (10 + 5) 

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet) 

# Same effect 
x = 0 
x += 1 
x = x + 1 

# Logical Operators 
print(3 > 5 and  4 < 3) # AND requires ALL expressions to be TRUE 
print (3 > 2 and 4 < 3)
print( 3 > 4 and 2 != 3) and favColor == "Blue" an temp == -5 
# When writing and expressions, put the value most likely to be fals first ! 

#Logical OR -- Requires ONE expression to be True.
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combined 
print( 3 > 2 and 4 < 3 or 5 != 7 )
#print(True and False or True )

# NOT Logical Operator 
print(not (3 > 2))
print(not (not (not (51= 3))))
