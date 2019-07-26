n=input()
arr=input().split()
min=2
ele=0
for i in arr:
	co=arr.count(i)
	if co<min:
		min=co
		ele=i
print(ele)
