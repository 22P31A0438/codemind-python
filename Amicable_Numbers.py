n=int(input())
m=int(input())
r=0
q=0
for i in range(1,n):
    if(n%i==0):
        r=r+i
for j in range(1,m):
    if(m%j==0):
        q=q+j
if(r==m and q==n):
    print("Amicable")
else:
    print("Not Amicable")
        