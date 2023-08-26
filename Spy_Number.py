n=int(input())
q=n
s=0
d=1
while(q>0):
    r=q%10
    q=q//10
    s=s+r
    d=d*r
if(s==d):
    print("Spy Number")
else:
    print("Not Spy Number")
