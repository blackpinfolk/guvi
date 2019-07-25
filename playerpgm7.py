arr=list(input())			#Input recieved
for i in range(len(arr)):
	if i%2==0:
		a=arr[i]
		b=arr[i+1]
		arr[i]=b
		arr[i+1]=a
print(*arr)
