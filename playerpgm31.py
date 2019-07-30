arr=list(input())
op=0
clo=0
for i in arr:
	if i=="(":
		op+=1
	elif i==")":
		clo+=1
print("yes" if op==clo else "no")
