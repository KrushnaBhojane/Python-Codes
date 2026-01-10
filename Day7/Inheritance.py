"""class A:                    #Single Inheritance
    num=10
    def show(self):
        print("It is A class..")
        print("num=",self.num)
class B(A):
    def paint(self):
        print("It is B class..")    
        print("num=",self.num)
b=B()   
b.show()
b.paint()"""

"""class A:                    #Multilevel Inheritance
    num=10
    def show(self):
        print("It is A class..")
        print("num=",self.num)  
class B(A):
    def paint(self):
        self.num=20
        print("It is B class..")    
        print("num=",self.num)  
class C(B):
    def display(self):
        print("It is C class..")    
        print("num=",self.num)
b=C()   
b.show()
b.paint()
b.display()"""

"""class A:                    #Hierarchical Inheritance
    num=10
    def show(self):
        print("It is A class..")
        print("num=",self.num)  
class B(A):                   #B class inherits A class
    def paint(self):
        self.num=20
        print("It is B class..")    
        print("num=",self.num)
class C(A):                   #C class inherits A class
    def display(self):
        print("It is C class..")    
        print("num=",self.num)
b=B()   
b.show()    
c=C()   
c.show()
c.display()"""

"""class A:                    # Multiple Inheritance
    num = 10
    def show(self):
        print("It is A class..")
        print("num =", self.num)

class B:
    num = 30
    def paint(self):
        print("It is B class..")
        print("num =", self.num)

class C(A, B):
    n = 50
    def display(self):                 
        print("It is C class..")
        print("num =", self.num)
        print("n =", self.n)

c = C()
c.show()
c.paint()
c.display()"""

class A:                    # Hybrid Inheritance
    num = 10
    def show(self):
        print("It is A class..")
        print("num =", self.num)            
class B(A):
    num = 30
    def paint(self):
        print("It is B class..")
        print("num =", self.num)

class C:
    n1=40
    def display(self):
        print("It is C class..")
        print("n1 =", self.n1)
class D(B,C):
    n=5
    def put(self):
        print("It is D class..")
        print("num =", self.num)
        print("n =", self.n)
        print("n1 =", self.n1)
c=D()
c.show()
c.paint()
c.display()
c.put() 
