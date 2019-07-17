newer=list(map(int,input()))
k=1
for i in newer:
	if i==1:
		pass
	elif i==0:
		pass
	else:
		k=0
		break
print("yes" if k==1 else "no")
