n=int(input())
s=n*n
f=0
while(n>0):
    if(n%10!=s%10):
        print("Not an Automorphic Number")
        f=1
        break
    n=n//10
    s=s//10
if(f==0):
    print("Automorphic Number")