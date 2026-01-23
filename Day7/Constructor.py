"""class student:                   #constructor
    def __init__(self):
        self.roll_no=1
        self.name="Krishna"
    def show(self):
        print("Student roll_no:",self.roll_no)
        print("Student name:",self.name)    
s=student()
s.show()"""

class student:                       #parameterized constructor
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
    def show(self):
        print("Student roll_no:",self.roll_no)
        print("Student name:",self.name)
r=int(input("Enter roll no:"))
n=input("Enter name:")
s=student(r,n)  
s.show()