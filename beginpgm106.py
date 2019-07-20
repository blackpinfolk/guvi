numer,num=list(map(int,input().split()))
arr=list(map(int,input().split()))
ar=[]
for i in arr:
	if i%2!=0:
		ar.append(i)
print(ar[num-1])
