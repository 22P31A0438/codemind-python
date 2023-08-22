n=int(input())
s=0
for i in range(2,n):
    if(n%i==0):
        s=1
        print("Not Prime")
        break;
    if(s==0):
        print("Prime")
        break;