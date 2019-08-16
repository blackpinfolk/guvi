n,k=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(1,k):
	ans=min(arr)
	arr.remove(min(arr))
print(min(arr))
