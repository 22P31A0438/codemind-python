n=int(input())
if(n<199):
    c=1.20
elif(n>=200 and n<400):
    c=1.40
elif(n>=400 and n<600):
    c=1.60
elif(n>=600 and n<800):
    c=1.80
else:
    c=2.00
b=c*n
if(b>400):
    s=b*0.15
else:
    s=0
t=b+s
print(f"Units Consumed: {n}
Cost per Unit: {c:.2f}
Bill: {b:.2f}
Surcharge: {s:.2f}
Total Amount: {t:.2f}")

