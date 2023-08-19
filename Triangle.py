a,b,c=map(int,input().split())
if(a==b==c):
    print("Equilateral triangle")
elif(a==b or b==c or a==c ):
    print("Isosceles triangle")
else:
    print("Scalene triangle")