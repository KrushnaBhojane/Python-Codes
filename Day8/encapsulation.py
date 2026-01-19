class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        if(age>0):
            self.__age=age
        else:
            print("Age cannot be negative")
p=person("Jayesh",21)
print("Name: ",p.get_name())
print("Age: ",p.get_age())
p.set_name("Krishna")
p.set_age(25)
print("Updated Name: ",p.get_name())
print("Updated Age: ",p.get_age())
p.set_age(-5)