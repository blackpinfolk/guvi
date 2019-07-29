arr=list(input())
i=0
j=0
while(i<len(arr) and j+1<len(arr)):
		if arr[i]==' ' and arr[j+1]==' ':
			del arr[i]
			i-=1
			j-=1
		elif arr[i]!=' ' and j+1==(len(arr)):
			del arr[j+1]
		i+=1
		j+=1
print(*arr,sep="")
