"""def add(p,q,r=0):        #function overloading
    return p + q + r
print(add(5,2))          
print(add(3,2,5))"""

class Animal:                     #method overriding
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animal=[Dog(),Cat(),Animal()]
for i in animal:
    i.sound()