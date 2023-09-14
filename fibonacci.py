n=int(input())
a=0
b=1
c=a+b
print(a,b,end=' ')
while(n-2>0):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
    n=n-1