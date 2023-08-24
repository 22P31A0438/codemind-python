n=int(input())
q=n
s=0
while(q!=0):
    r=q%10
    s=s*10+r
    q=q//10
print(s)