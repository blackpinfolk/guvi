n=int(input())
arr=list(map(int,input().split()))
a=[]
for i in range(n):
	if i%2==0 and arr[i]%2!=0 :
		a.append(arr[i])
	elif i%2!=0 and arr[i]%2==0:
		a.append(arr[i])
print(*a,sep=" ")
