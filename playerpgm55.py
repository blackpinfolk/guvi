arr,nrr=map(str,input().split())
arr=list(arr)
nrr=list(nrr)
for i in range(len(arr)):
	if (str(arr[i]).lower())==(str(nrr[i]).lower()):
		pass
	else:
		print("no")
		exit()
print("yes")
