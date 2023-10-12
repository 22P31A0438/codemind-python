n,r,d=map(int,input().split())
if(r>n and d>n):
    print(r+d)
elif(n>r and d>r):
    print(n+d)
else:
    print(n+r)