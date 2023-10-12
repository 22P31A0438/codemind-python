n=int(input())
if(n%5==0):
    if n%10==0:
        print(n//10)
    else:
        print(n//10+1)
else:
    print("-1")
        