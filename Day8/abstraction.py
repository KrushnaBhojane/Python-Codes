from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("Animal is sleeping")
class Dog(Animal):
    def sound(self):
        return "Barks"
class Cat(Animal):
    def sound(self):
        return "Meows"
dog=Dog()
cat=Cat()
print(f"Dog: {dog.sound()}")
print(f"Cat: {cat.sound()}")
dog.sleep()