numer=list(input())
a=[]
for i in numer:
	if ord(i)<58 and ord(i)>47:
		a.append(i)
print(*a,sep="")
