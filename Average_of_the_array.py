n=int(input())
num=list(map(int,input().split()))
s=0
for i in num:
    s=s+i
d=s/n
print(f"{d:.2f}")