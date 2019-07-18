n=int(input())
arr=list(map(int,input().split()))
lo=list(map(abs,arr))
low=sum(lo)
yeah=0
for i in range(n):
	for j in range(n):
		if i!=j:
			if arr[i]+arr[j]==0:
				print(arr[i],arr[j],sep=" ")
				yeah=1
				exit()
			else:
				val=arr[i]+arr[j]
				val=abs(val)
				if val<low:
					low=val
					low1=arr[i]
					low2=arr[j]
if yeah==0:
	print(low1,low2,sep=" ")
else:
	pass
