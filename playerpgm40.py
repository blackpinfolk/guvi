n=int(input())
a=0
if n%2!=0:
	a=1
b=n//2
count=0
while(a<=n and b>=0):
	if (a*1)+(b*2)==n:
		count+=1
	if n%2==0:
		a+=2
	else:
		a+=2
	b-=1
print(count)
