n=input()
arr=list(map(str,input().split()))
ar=[]
kr=[]
arr=sorted(arr)
for i in range(len(arr)):
	ar.append(len(arr[i]))
for i in range(len(arr)):
	mini=min(ar)
	ind=ar.index(mini)
	kr.append(arr[ind])
	ar[ind]=max(ar)+1
print(*kr)
