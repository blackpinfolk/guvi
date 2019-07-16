n=[]
k=[]
for i in range(2):
	x,y=map(int,input().split())
	n.append(x)
	k.append(y)
print(abs(n[0]-n[1]),abs(k[0]-k[1]),sep=' ')
