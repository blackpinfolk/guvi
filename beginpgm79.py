new,mew=map(int,input().split())
pro=new*mew
yeah=0
for i in range(pro):
	if i**2==pro:
		yeah=1
		break
print("yes" if yeah==1 else "no")
