new=int(input())
yeah=1
for i in range(2,new):
	if new%i==0:
		yeah=0
		break
print("yes" if yeah==0 else "no")
