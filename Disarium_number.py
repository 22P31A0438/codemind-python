n=int(input())
s=0
j=n
while(j):
    r=j%10
    j=j//10
    s=s*10+r
p=0
i=1
while(s):
    t=s%10
    s=s//10
    p=p+(t**i)
    i+=1
if(p==n):
    print("True")
else:
    print("False")
    
        