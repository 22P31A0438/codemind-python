n=int(input())

while True:
    s = 0
    q = n
    while(q!=0):
        r=q%10
        s=s+r
        q=q//10
    if s>9:
        n = s
    else:break
    
print(s)