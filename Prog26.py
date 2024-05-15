n=int(input("Enter limit: "))
a,b=0,1
print(a,b,end=' ')
i=0
while (i<n-2):
    c=a+b
    print(c, end=' ')
    a=b
    b=c
    i=i+1
