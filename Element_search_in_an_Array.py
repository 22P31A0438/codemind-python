n=int(input())
num=list(map(int,input().split()))
c=0
m=int(input())
for i in num:
    if(m==i):
        c=c+1
        break
if(m==i):
    print("True")
else:
    print("False")