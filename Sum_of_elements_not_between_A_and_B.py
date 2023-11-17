n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(n):
    if l[i]<a or l[i]>b:
       c=c+l[i]
print(c)
        