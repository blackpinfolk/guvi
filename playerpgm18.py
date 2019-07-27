n=int(input())
krr=['k','a','b','a','l','i']
count=0
arr=[]
for i in range(n):
	a=input()
	arr.append(a)
for i in range (len(arr)):
	ar=list(arr[i])
	if len(ar)==6:
		for j in range(len(ar)):
			if krr[j] in ar:
				ar.remove(krr[j])
		if len(ar)==0:
			count+=1
print(count)
