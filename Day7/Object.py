""""class student:
    roll_no= 1 
    name= "Krishna"
    def show(self):
        print("Student roll_no:",self.roll_no)
        print("Student name:",self.name)
s=student()
s.show()"""

class student:
    roll_no= 0 
    name= 0
    def accept(self):
        self.roll_no= int(input("Enter roll no:"))
        self.name= input("Enter name:")
    def show(self):
        print("Student roll_no:",self.roll_no)
        print("Student name:",self.name)
s=student()
s.accept()  
s.show()