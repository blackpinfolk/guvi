newer9=int(input())
k=1
i=2
while(i<newer9):
	if(newer9%i==0):
		k=0
		break
	i+=1
print("yes" if k==1 and newer9>1 else "no")
