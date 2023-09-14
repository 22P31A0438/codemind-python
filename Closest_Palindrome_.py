def clopal(n):
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
while not clopal(i) and not clopal(j):
    i=i+1
    j=j-1
if(clopal(i) and clopal(j)):
    if(abs(i-n)==abs(n-i)):
        print(j,i)
    else:
        if(abs(i-n)>abs(n-j)):
            print(j)
        else:
            print(i)
elif(clopal(i)):
        print(i)
else:
    print(j)
        