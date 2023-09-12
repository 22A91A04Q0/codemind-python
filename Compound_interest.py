p,r,t=map(int,input().split())
n=p*pow((1+r/100),t)
print(f"{n:.2f}")