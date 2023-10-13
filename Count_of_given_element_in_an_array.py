n=int(input())
c=0
num=list(map(int,input().split()))
m=int(input())
for i in num:
    if(m==i):
        c=c+1
print(c)
    