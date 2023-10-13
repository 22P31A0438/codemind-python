n=int(input())
s=0
c=0
num=list(map(int,input().split()))
for i in range(n):
    if(num[i]%2 == 0):
        s += num[i]
    else:
        c += num[i]
d=abs(s-c)
print(d)