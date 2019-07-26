start,end=list(map(int,input().split()))
count=0
for j in range(start,end+1):
	i=2
	yeah=1
	while(j>i):
		if(j%i==0):
			yeah=0
			break
		i+=1
	if yeah==1:
		count+=1
print(count)
