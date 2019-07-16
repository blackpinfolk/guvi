n=input()
co=0
for i in n:
	if i.isnumeric():
		pass
	elif i.isalpha():
		pass
	elif i.isspace():
		pass
	else:
		co+=1
print(co)
