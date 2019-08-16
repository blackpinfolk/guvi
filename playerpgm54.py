arr,nrr=map(str,input().split())
arr=list(arr)
nrr=list(nrr)
for i in range(len(arr)):
	if arr[i]==nrr[i]:
		pass
	else:
		print("no")
		exit()
print("yes")
