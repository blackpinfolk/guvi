n=int(input())
arr=[]
ar=[]
yeah=1
for i in range(2,n+1):
	if n%i==0:
		arr.append(i)
for j in arr:
	yeah=1
	for i in range(2,j):
		if j%i==0:
			yeah=0
			break
	if yeah!=0:
		ar.append(j)
print(*ar,sep=" ")
