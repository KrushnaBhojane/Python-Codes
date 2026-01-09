n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

def calc(a, b):
    return a + b, a - b, a * b

x, y, z = calc(n1, n2)

print("Sum:", x)
print("Difference:", y)
print("Product:", z)
