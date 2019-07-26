arr=list(map(str,input()))
max=0
for i in arr:
	co=arr.count(i)
	if co>max:
		max=co
		ele=i
print(ele)
