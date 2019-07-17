n=int(input())
arr=list(map(int,input().split()))
krr=[]
yeah=0
for i in range(n):
	if arr[i] in krr:
		yeah=1
		ans=arr[i]
		break
	else:
		krr.append(arr[i])
if(yeah==1):
	print(ans)
else:
	print("unique")
