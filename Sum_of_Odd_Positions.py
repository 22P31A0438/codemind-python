n=int(input())
s=0
num=list(map(int,input().split()))
for i in range(1,n,2):
        s=s+num[i]
print(s)