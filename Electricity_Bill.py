n=int(input())
if(n<199):
    s=1.20
elif(n>=200 and n<400):
    s=1.40
elif(n>=400 and n<600):
    s=1.60 
elif(n>=600 and n<800):
    s=1.80
else:
    s=2.00
b=n*s
c=0
if(b>400):
    c=b*0.15
t=b+c
print(f"Units Consumed: {n}
Cost per Unit: {s:.2f}
Bill: {b:.2f}
Surcharge: {c:.2f}
Total Amount: {t:.2f}")