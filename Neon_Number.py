n=int(input())
s=0
c=n*n
while(c>0):
    r=c%10
    c=c//10
    s=s+r
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")