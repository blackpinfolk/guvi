arr=list(map(str,input().split()))
for i in range(len(arr)):
	k=list(arr[i])
	k.reverse()
	print(*k,sep="",end=" ")
