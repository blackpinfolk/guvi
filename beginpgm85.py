arr=list(input())
odd=[]
even=[]
for i in range(len(arr)):
	if i%2!=0:
		odd.append(arr[i])
	else:
		even.append(arr[i])
print(*even,sep="",end=" ")
print(*odd,sep="",end=" ")
