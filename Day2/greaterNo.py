a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))
if a>b and a>c:
    print(f"{a} is the Greatest Number")
elif b>c and b>a:
    print(f"{b} is the Greatest Number")
elif c>a and c>b:
    print(f"{c} is the Greatest Number")
else:
    print("All are Equal")