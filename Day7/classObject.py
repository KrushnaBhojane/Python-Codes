"""class student:
    roll_no=2
    name="Jayesh"
    def show(self):
        print("Student roll_no: ",self.roll_no)
        print("Student name: ",self.name)

s=student()
s.show()"""

#take input from user and create object
class student:
    roll_no=0
    name=0
    def accept(self):
        self.roll_no=int(input("Enter roll no: "))
        self.name=input("Enter the the name of student: ")
    def show(self):
        print("Student Roll_No: ",self.roll_no)
        print("Student Name: ",self.name)
s=student()
s.accept()
s.show()