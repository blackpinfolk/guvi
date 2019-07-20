ini,dif,num=list(map(int,input().split()))
a=[]
for i in range(num):
	a.append(ini)
	ini=ini+dif
print(sum(a))
