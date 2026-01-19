class A:
    num=10
    def show(self):
        print("It is a A class method")
        print("Number=", self.num)
class B:
    n=20
    def paint(self):
        print("It is a B class Method")
        print("Number=", self.n)
class C(A,B):
    def display(self):
        print("It is a C class Method")
        print("Number=", self.num)
c=C()
c.show()
c.display()
c.paint()

