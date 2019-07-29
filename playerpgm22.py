x,y=list(map(int,input().split()))
max=x
min=y
if y>x:
	max=y
	min=x
for i in range(1,min+1):
	if max%i==0 and min%i==0:
		ans=i
print(ans)
