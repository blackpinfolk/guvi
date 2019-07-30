start,last=list(map(int,input().split()))
arr=[]
count=0
for i in range(last):
	arr.append(i*i)
for i in range(start,last+1):
	if i in arr:
		count+=1
print(count)
