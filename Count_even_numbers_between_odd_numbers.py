n=int(input())
num=list(map(int,input().split()))
c=0
for i in range(0,n-2):
    if(num[i]%2!=0 and num[i+1]%2==0 and num[i+2]%2!=0):
        c=c+1
print(c)