arr=list(input())
for i in range(len(arr)):
	if arr[i]=='X':
		arr[i]='A'
	elif arr[i]=='Y':
		arr[i]='B'
	elif arr[i]=='Z':
		arr[i]='C'
	else:
		arr[i]=chr(ord(arr[i])+3)
print(*arr,sep="")
