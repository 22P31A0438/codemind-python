def ug(n):
    if n==0:
        return False
    for i in [2,3,5]:
        while (n%i==0):
            n=n/i
    if(n==1):
        return 1
    else:
        return 0
a=int(input())
if(ug(a)==1):
    print("Ugly Number")
else:
    print("Not Ugly Number")