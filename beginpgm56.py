numer=list(input())
a=0
d=0
for i in numer:
	if i.isalpha():
		a+=1
	elif i.isdigit():
		d+=1
print("Yes" if a and d >0 else "No")
