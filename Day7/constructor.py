"""class student:
    def __init__(self):
        self.name="Jayesh"
        self.roll_no=25
    def show(self):
        print("Student Name: ",self.name)
        print("Student Roll_No: ",self.roll_no)

s1=student()
s1.show()"""

#take input from user and use parametric consrtructor.
class student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    def show(self):
        print("Student Roll_No: ",self.roll_no)
        print("Student Name: ",self.name)
r=int(input("Enter roll no: "))
n=input("Enter the name of student: ")
s=student(r,n)
s.show()