newer=list(input())
le=len(newer)
if le%2==0:
	d=le//2
	newer[d-1]=newer[d]='*'
else:
	d=le//2
	newer[d]='*'
print(*newer,sep="")
