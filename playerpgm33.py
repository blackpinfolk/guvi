n=int(input())
ar=[]
count=0
for i in range(n):
	arr=list(map(int,input().split()))
	ar.append(arr)
for i in range(n):
	for j in range(n):
		set1=0
		set2=0
		set3=0
		set4=0
		if ar[i][j]==1:
			if i+1<n:
				if (ar[i+1][j]==0):
					set1=1
			elif i+1>=n:
				set1=1
			if j+1<n:
				if (ar[i][j+1]==0):
					set2=1
			elif j+1>=n:
				set2=1
			if i-1>=0:
				if (ar[i-1][j]==0):
					set3=1
			elif i-1<=0:
				set3=1
			if j-1>=0:
				if (ar[i][j-1]==0):
					set4=1
			elif j-1<=0:
				set4=1
		if set1==set2==set3==set4==1:
			count+=1
print(count)
