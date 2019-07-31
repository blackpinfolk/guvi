arr=list(input())
ar=[]
for i in arr:
	if i==" ":
		arr.remove(i)
for i in range(len(arr)):
	ar.append(arr.count(arr[i]))
n=ar.count(min(ar))
for i in range(n):
	k=ar.index(min(ar))
	print(arr[k],end=" ")
	ar[k]=max(ar)
