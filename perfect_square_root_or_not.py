import math
n=int(input())
for i in range(1,int((math.sqrt(n))+1)):
    c=0
    if(i*i==n):
        c=1
if(c==1):
    print("True")
else:
    print("False")