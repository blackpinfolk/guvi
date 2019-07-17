numer1=int(input())
k=1
for i in range(1,numer1):
	if 2**i==numer1:
		print("yes")
		k=0
if (k!=0):
	print("no")
