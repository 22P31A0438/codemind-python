n=int(input())
if(n<=199):
    b=n*1.20
elif(n>=200 and n<400):
    b=n*1.50
elif(n>=400 and n<600):
    b=n*1.80
else:
    b=n*2.00
if(b>400):
    sc=b*0.15
    t=sc+b
else:
    sc=100
    t=sc+b
print(f"{t:.2f}")
    
    