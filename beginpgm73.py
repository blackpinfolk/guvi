numer1=int(input())
l,r=map(int,input().split())
l+=1
yeah=0
if numer1 in range(l,r):
	yeah=1
print("yes" if yeah==1 else "no")
