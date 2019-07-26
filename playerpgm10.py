arr,ar=list(map(str,input().split()))
ar=list(map(str,ar))
arr=list(map(str,arr))
count=0
for i in range(len(arr)):
	if arr[i]!=ar[i]:
		count+=1
print("yes" if count==1 else "no")
