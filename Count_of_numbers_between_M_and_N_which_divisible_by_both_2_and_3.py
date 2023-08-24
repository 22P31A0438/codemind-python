n,m=map(int,input().split())
s=0
for i in range(n,m+1):
    if(i%2==0 and i%3==0):
        s=s+1
print(s)