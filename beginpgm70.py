new=int(input())

for i in range(2+new):
	if 2**i>new:
		k=2**i
		break
print(k)
