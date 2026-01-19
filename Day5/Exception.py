"""a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
try:
    c=a//b
    print("Dividion is: ",c)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero.",e)
finally:
    print("This is a Finally block which will always execute.")
def msg():
    print("This is a function message.")
msg()"""
Number = 10
try:
    print("The number is:",Numer)
except NameError as i:
    print("Message:",i)