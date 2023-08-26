n=int(input())
m=int(input())
for i in range(n,m+1):
    j=i
    c=0
    while(j>0):
        r=j%10
        j=j//10
        if(r>0 and i%r==0):
            c+=1
    if(c==len(str(i))):
        print(i,end=' ')
    