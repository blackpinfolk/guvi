arr=list(input())			#Input recieved
for i in range(len(arr)):
	if i%2==0:			#Even number condition
		a=arr[i]		
		b=arr[i+1]		#Swapped
		arr[i]=b
		arr[i+1]=a
print(*arr)
