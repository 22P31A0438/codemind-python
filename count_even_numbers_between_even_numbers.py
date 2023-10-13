n=int(input())
c=0
num=list(map(int,input().split()))
for i in range(0,(n-2)):
    if(num[i]%2==0 and num[i+2]%2==0 and num[i+1]%2==0):
        c=c+1
print(c)