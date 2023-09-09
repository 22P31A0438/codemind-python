c,d=map(int,input().split())
a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
to=a1+a2+a3
tm=b1+b2+b3
if(to>=150 and tm>=150):
    s=to+tm+d
elif(to>=150 and tm<150):
    s=to+tm+c+d
elif(to<150 and tm>=150):
    s=to+tm+c+d
else:
    s=to+tm+c+c+d
if(s>=to+tm+c+c):
    print("NO")
else:
    print("YES")