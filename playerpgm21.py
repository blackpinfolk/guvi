x1,y1=list(map(int,input().split()))
x2,y2=list(map(int,input().split()))
x3,y3=list(map(int,input().split()))
x1=int(x1)
x2=int(x2)
x3=int(x3)
y1=int(y1)
y2=int(y2)
y3=int(y3)
a=x1*(y2-y3)+x2*(y1-y3)+x3*(y1-y2)
if a==0:
	print("yes")
else:
	print("no")
