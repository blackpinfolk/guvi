n,k=map(int,input().split())
i=0
while(k**i<=n):
	if k**i==n:
		print("yes")
		exit()
	i+=1
print("no")
