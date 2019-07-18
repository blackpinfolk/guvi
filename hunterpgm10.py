n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
ar=list(map(int,input().split()))
yeah=0
for i in range(m):
	if ar[i] in arr:
		arr.remove(ar[i])
		yeah=1
	else:
		print("NO")
		exit()
if yeah==1:
	print("YES")
