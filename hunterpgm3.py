n1=int(input())
arr=list(map(int,input().split()))
a=[]
yeah=0
for i in range(n1):
	if(arr[i]==i):
		a.append(i)
		yeah=1
	else:
		pass
if yeah==1:
	a=list(sorted(a))
	print(*a)
else:
	print(-1)
