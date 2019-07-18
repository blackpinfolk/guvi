n,m=list(map(int,input().split()))
low=n
if m<n:
	low=m
else:
	pass
for i in range(1,low+1):
	if n%i==0 and m%i==0:
		k=i
print(k)
