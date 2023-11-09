n=int(input())
m=[list(map(int,input().split())) for i in range(n)]
r=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j]=m[i][j]+r[i][j]
for i in m:
    for j in i:
        print(j,end=" ")
    print()