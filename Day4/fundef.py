def square(num1,num2):
    return num1 ** num2

a=int(input("Enter the number:"))
b=int(input("Enter the power:"))
result = square(a,b)
print(f"The result of {a} raised to the power of {b} is {result}")