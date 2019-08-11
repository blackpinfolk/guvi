a=input()
cou=a.count(",")
for i in range(cou):
	a=a.replace(",","")
print(a)
a=int(a)
if (a<=2**15+1) and (a>=-2**15+1):
	print("INT")
else:
	print("LONG")
