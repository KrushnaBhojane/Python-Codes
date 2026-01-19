class A:
    num=10
    def show(self):
        print("It is a A class method")
        print("Number=", self.num)
class B(A):
    def paint(self):
        print("It is a B class Method")
        print("Number=", self.num)
class C:
    n1=50
    def display(self):
        print("It is a C class Method")
        print("Number=", self.n1)
class D(B,C):
    def put(self):
        print("It is a D class Method")
        print("Number=", self.num)
        print("n1=",self.n1)
d=D()
d.show()
d.display()
d.paint()
d.put()