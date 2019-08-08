cou=0
for i in range(int(input())):
	a,b=map(int,input().split())
	if a<b:
		cou+=1
print(cou)
