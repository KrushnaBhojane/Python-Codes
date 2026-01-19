a,b =0,1
print(a,b,end=" ")
i=2
while i<10:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i=i+1