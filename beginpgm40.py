n=int(input())
if n!=0:
	print(1,end=' ')
	j=1
	k=0
	for i in range(1,n):
		z=k+j
		print(z,end=' ')
		k=j
		j=z
else:
	print(0)
