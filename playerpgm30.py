start,last,k=list(map(str,input().split()))
count=0
start=list(start)
last=list(last)
for i in range(len(start)):
	if start[i]!=last[i]:
		count+=1
print("yes" if count==int(k) else "no")
