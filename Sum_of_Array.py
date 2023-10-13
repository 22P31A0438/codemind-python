n=int(input())
s=0
num=list(map(int,input().split()))
for i in range(n):
    s=s+num[i]
print(s)