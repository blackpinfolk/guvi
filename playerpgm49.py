a=input()
cou=a.count(",")
for i in range(cou):
	a=a.replace(",","")
a=int(a)
if (a<=2**15+1) and (a>=-2**15+1):
	print("INT")
elif (a<=2**31+1) and (a>=-2**31+1):
	print("LONG")
else:
	print("LONG LONG")
