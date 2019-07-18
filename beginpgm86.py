arr=list(input())
yeah=1
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		if arr[i]==arr[j]:
			print("No")
			yeah=0
			exit()
		else:
			pass
if yeah==1:
	print("Yes")
