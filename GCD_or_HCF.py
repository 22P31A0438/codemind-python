n,m=map(int,input().split())
if(n<m):
    s=n
else:
    s=m
for i in range(1,s+1):
    if(n%i==0 and m%i==0):
        g=i
print(g)