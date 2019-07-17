new,old=list(map(int,input().split()))
k=abs(new-old)
print("even" if k%2==0 else "odd")
