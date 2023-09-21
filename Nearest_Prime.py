def prm(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
while(n):
    m=int(input())
    for i in range(1,m+1):
        if(prm(i)):
            a=i
    i=m+1
    while(1):
        if(prm(i)):
            b=i
            break
        i=i+1
    x=abs(a-m)
    y=abs(b-m)
    if(x<y):
        print(a)
    elif(x==y):
        print(a)
    else:
        print(b)
    n=n-1