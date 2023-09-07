n=int(input())
s=0
while(n):
    r=n%10
    if(s<r):
        s=r
    n=n//10
print(s)