"""
print("The Length is: ",len("Jayesh"))
def add(p,q,r=0):
    return p+q+r
print("Addition using Two Variable: ",add(10,20))
print("Addition using three variable: ",add(10,20,30))
"""

# Polymorphism using method overriding
class Animal:
    def sound(self):
        print("Animal makes a sounds")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
animal=[Animal(),Dog(),Cat()]
for i in animal:
    i.sound()