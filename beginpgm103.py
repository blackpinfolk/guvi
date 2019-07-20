arr=list(input())
yeah=1
h=0
for i in arr:
	if i==' ':
		yeah=1
	elif yeah==1:
		yeah=0
		arr[h]=i.upper()
	else:
		pass
	h+=1
print(*arr,sep="")
