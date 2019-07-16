n=int(input())
i=2
k=1
while(i<n):
	if(n%i==0):
		k=0
		break
	else:
		i+=1
if k==0:
	print("no")
else:
	print("yes")
