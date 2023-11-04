m,n=map(int,input().split())
s=0
num=[list(map(int,input().split()))[:n:] for i in range(m)]
for i in num:
    for j in i:
        s=s+j
print(s)