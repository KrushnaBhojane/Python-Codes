'''file=open("Simple.txt","w")
file.write("Hello World!\n")
file.close()'''

"""file=open("Simple.txt","r")
data=file.read()
print(data)
file.close()"""

try:
    f=open("Simple.txt","a")
    f.write("Welcome to File Handling in Python.\n")
    f.close()
except FileNotFoundError as e:
    print("Error:",e)