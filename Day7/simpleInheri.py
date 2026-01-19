class A:
    num=10
    def show(self):
        print("It is a A class method")
        print("Number=", self.num)
class B(A):
    def paint(self):
        print("It is a B class Method")
        print("Number=", self.num)
b=B()
b.show()
b.paint()

