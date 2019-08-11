p,a=map(int,input().split())
for i in range(p):
	for j in range(a):
		if (2*(i+j)==p) and (i*j==a):
			print("yes")
			exit()
print("no")
