x,y=input().split()
s1=0
s2=0
for i in range(len(x)):
	s1+=ord(x[i])
for i in range(len(y)):
	s2+=ord(y[i])
if(s1>s2):
	print(x)
elif(s2>s1):
	print(y)
else:
	print(x)
