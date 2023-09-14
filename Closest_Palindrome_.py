def clo(n):
    j=n
    s=0
    while(j>0):
        r=j%10
        j=j//10
        s=s*10+r
    if(s==n):
        return True
    else:
        return False
n=int(input())
i=n+1
j=n-1
while not clo(i) and not clo(j):
    i=i+1
    j=j-1
if(clo(i) and clo(j)):
    if(abs(n-i)==abs(i-n)):
        print(j,i)
    else:
        if(abs(i-n)>abs(n-j)):
            print(j)
        else:
            print(i)
elif(clo(i)):
    print(i)
else:
    print(j)
