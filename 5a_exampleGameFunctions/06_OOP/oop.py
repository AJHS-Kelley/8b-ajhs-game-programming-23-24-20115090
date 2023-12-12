# Object-Oriented Programming, Jordan Henry, v0.0

class Person: # Use PascalCase for ClassNames 
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight 

# To string function -- How the object appears as a string 
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight}pounds.\n"




person1 = Person("Chris",30, 195)
print(person1)