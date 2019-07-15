n,k=input().split(" ")
arr=input().split(" ")
for i in range(0,len(arr)):
	arr[i]=int(arr[i])
k=int(k)
sum=0
for i in range(0,k):
	sum=sum+arr[i]
print(sum)
