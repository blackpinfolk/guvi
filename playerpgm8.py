arr=list(input())			#Input Recieved
arr[0]=str(arr[0]).upper()	#1st word Capitalized
yeah=1
for i in range (len(arr)):
	if arr[i]==' ':
		yeah=0
	elif yeah==0:	
		yeah=1
		arr[i]=(str(arr[i])).upper()		#Words first letter Captalized
print(*arr,sep="")
