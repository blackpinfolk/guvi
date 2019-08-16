arr,a=map(str,input().split())
arr=list(arr)
j=1
for i in arr:
	if i==a:
		break
	j+=1
print(j)
