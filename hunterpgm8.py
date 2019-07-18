n=int(input())
arrr=list(map(int,input().split()))
for i in range (len(arrr)):
	for j in range (i+1,len(arrr)):
		for k in range (j+1,len(arrr)):
			if arrr[i]+arrr[j]==arrr[k]:
				print(arrr[i],arrr[j],arrr[k],sep=" ")
