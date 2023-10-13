n=int(input())
s=0
num=list(map(int,input().split()))
for i in range(n):
    if(num[i]%2!=0):
        s=s+num[i]
print(s)