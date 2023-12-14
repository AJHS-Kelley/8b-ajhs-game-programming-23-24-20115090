# Object-Oriented Programming, Jordan Henry, v0.0

class Person: # Use PascalCase for ClassNames 
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight 
        self.weakness = None
        self.nemesis = none

# To string function -- How the object appears as a string 
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight}pounds.\n"
    
    def ClassFunction():
        print("This is an example class function.\n")
        print("It only works when called on an object of that class.")





person1 = Person("Chris",30, 195)
person2 = Person("Angel", 16, 140)
print(person1) 
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name} weighs more than {person2.weight}.")
elif person1.weight == person2.weight:
    print("Each person weighs the same.\n")
else: 
    print(f"{person2.name} weighs more than{person1.name}.") 

if person1.age > person2.age:
    print(f"{person1.age} is older than {person2.age}")
elif person1.age == person2.age:
    print("Each person is the same age.\n")
else: 
    print(f"{person2.age} is older than{person1.age}")

 person1.classFunction() 

# Changing properties after creation
print(person1.name)
person1.name = "William Butcher"
print(person1.name)

# Deleting Properties -- DANGER WILL ROBINSON, DANGER!
# THIS DOES NOT'RESET' A PROOPERTY, IT DELETES IT COMPLETELY
print(person1.name)
del person1.name
# print(person1)

# Deleting Objects -- Delete them if you think your finished with them
del person1

# Adding Properties to Objects -- USE CAREFULLY 
person2.weakness = "cryptonite"
print(person2)
print(person2.weakness)
