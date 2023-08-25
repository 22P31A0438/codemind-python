n=int(input())
r=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        r=r+i
if(r==n):
    print("True")
else:
    print("False")