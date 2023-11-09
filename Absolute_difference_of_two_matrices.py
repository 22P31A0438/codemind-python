n=int(input())
m=[list(map(int,input().split())) for i in range(n)]
r=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j]=abs(m[i][j]-r[i][j])
for i in m:
    for j in range(n):
        if(j != n-1):
            print(i[j],end=" ")
        else:
            print(i[j])