n,m=list(map(int,input().split()))
high=n
low=m
if m>n:
	high=m
	low=n
j=1
for i in range(high*low):
	if low*i==high*j:
		print(n*i)
		yeah=1
		exit()
	else:
		if low*(i+1)<high*j:
			pass
		elif low*(i+1)>high*j:
			j+=1
if n==m:
	print(n)
