n=int(input())
m=[list(map(int,input().split())) for i in range(n)]
r=[list(map(int,input().split())) for i in range(n)]
c=[m[j][k]+r[j][k] for j in range(n) for k in range(n)]
ind = 0
for i in range(n):
    for j in range(n):
        print(c[ind],end=" ")
        ind+=1
    print()