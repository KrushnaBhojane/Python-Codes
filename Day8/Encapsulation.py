class person:
    def __init__(self,name,age):
        #private attributes
        self.__name = name          
        self.__age = age    

#public method to get name
    def get_name(self):
        return self.__name       

#public method to set name
    def set_name(self,name):
        self.__name = name

#public method to get age
    def get_age(self):
        return self.__age

#public method to set age
    def set_age(self,age):
        if age>=0:        #Validating the age before setting
            self.__age = age
        else:
            print("Age cannot be negative!")

#Creating object of the person
person1=person("Krishna",21)

#Accessing private attributes through getting methods
print(person1.get_name())
print(person1.get_age())

#Modifying private 
person1.set_name("Krish")

#Accessing modified value
print(person1.get_name())
print(person1.get_age())

#Attempting to set negative age
person1.set_age(-5)