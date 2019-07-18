arr=list(input())
ar=['a','e','i','o','u']
yeah=0
for i in arr:
	if i in ar:
		yeah=1
	else:
		pass
print("yes" if yeah==1 else "no")
