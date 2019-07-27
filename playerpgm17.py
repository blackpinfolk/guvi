arr,ar=list(map(int,input().split()))
i=1
while(True):
	if (i%arr==0 and i%ar==0):
		print(i)
		exit()
	i+=1
