from abc import ABC, abstractmethod

class Animal(ABC):                     #abstract class
    @abstractmethod
    def sound(self):
        pass             #abstract method
    def sleep(self):                  #concrete method
        print("This Animal is sleeping")

class Dog(Animal):
    def sound(self):              #implementing abstract method
        return"Bark!"
    
class Cat(Animal):
    def sound(self):              #implementing abstract method
        return"Meow!"
#Instantiate Subclasses
dog=Dog()
cat=Cat()

print(f"Dog sound:{dog.sound()}")
print(f"Cat sound:{cat.sound()}")
dog.sleep() 
 
    
