ar,k=list(map(int,input().split()))
arr=input().split()
if(k%2==0):
	print(*arr)
elif (k%2!=0):
	print(*arr[-1:]+arr[:-1])
else:
	print(*arr[-k:]+arr[:-k])
