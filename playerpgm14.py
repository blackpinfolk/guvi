n=int(input())
arr=list(map(str,input()))
j=0
while(j<len(arr)):
	if (arr[j]=='a' or arr[j]=='A' or arr[j]=='e' or arr[j]=='E' or arr[j]=='i' or arr[j]=='I' or arr[j]=='o' or arr[j]=="O" or arr[j]=='u' or arr[j]=='U'):
		arr.remove(arr[j])
		j-=1
	j+=1
arr.reverse()
print(*arr,sep="")
