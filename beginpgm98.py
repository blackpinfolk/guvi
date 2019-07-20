num=int(input())
arr=list(map(int,input().split()))
le=len(arr)
j=0
for i in range(le):
	if (i+1)!=arr[i]:
		print(i)
		exit()
