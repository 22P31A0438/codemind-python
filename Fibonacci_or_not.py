n=int(input())
f=0
a=0
b=1
c=a+b
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    if(c==n):
        f=1
        print("True")
    else:
        c=c+1
if(f==0):
    print("False")