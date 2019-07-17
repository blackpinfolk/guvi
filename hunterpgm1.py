n=int(input())
arr=list(map(int,input().split()))
krr=[]
ans=[]
yeah=0
for i in range(n):
	if arr[i] in krr:
		yeah=1
		if arr[i] in ans:
			pass
		else:
			ans.append(arr[i])
	else:
		krr.append(arr[i])
ans=list(sorted(ans))
if(yeah==1):
	print(*ans)
else:
	print("unique")
