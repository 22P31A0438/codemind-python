a=int(input())
b=a//3600
c=(a-(b*3600))//60
d=a-(b*3600)-(c*60)
print(f"H:M:S-{b}:{c}:{d}")