arr,ar=input().split()			#Input recieved
ar=list(ar)
arr=list(arr)
yeah=1			#Temp variable
for i in range(len(arr)):
	if ar.count(ar[i])==arr.count(arr[i]):			#count of variable is compared
		pass
	else:
		yeah=0
print("yes" if yeah==1 else "no")
