def happy(n):
    f=n
    s1=0
    while(f>0):
        r=f%10
        s1=s1+(r*r)
        f=f//10
    return s1
n=int(input())
happy(n)
s=n
while(s>9):
    s=happy(s)
if(s==1 or s==7):
    print("True")
else:
    print("False")