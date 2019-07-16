n=input()
k=n.lstrip('-').replace('.','',1).isdigit()
if(k==True):
	print("yes")
else:
	print("No")
