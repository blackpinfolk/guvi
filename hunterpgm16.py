n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
ar=[]
for i in range(len(arr)):
	ar.append(abs(arr[i]-k))
ind=arr.index(k)
ar[ind]=max(arr)
for i in range(3):
	mi=ar.index(min(ar))
	print(arr[mi],end=" ")
	ar[mi]=max(arr)
