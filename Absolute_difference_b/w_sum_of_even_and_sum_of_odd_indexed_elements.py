n=int(input())
s=0
c=0
num=list(map(int,input().split()))
for i in range(1,n,2):
    s=s+num[i]
for j in range(0,n,2):
    c=c+num[j]
d=c-s
print(d)