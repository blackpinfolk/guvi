arr=list(input())
for i in range(len(arr)):
	if arr[i].isupper():
		arr[i]=arr[i].lower()
	elif arr[i].islower():
		arr[i]=arr[i].upper()
print(*arr,sep="")
