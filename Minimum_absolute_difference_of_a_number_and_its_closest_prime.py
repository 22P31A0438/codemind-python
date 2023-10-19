def prm(n):
    if(n==1):
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
n=int(input())
c=0
b=n
while(1):
    if(prm(n+c)==1):
        break
    c=c+1
while(n):
    if(prm(n)==1):
        break
    n=n-1
if(b-n>c):
    print(c)
else:
    print(b-n)