n,m,r=map(int,input().split())
s=(n/(m*r))
if(s==int(s)):
    print(int(s))
else:
    print(int(s)+1)