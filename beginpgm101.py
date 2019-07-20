lis,num=input().split()
lis=list(lis)
num=int(num)
en=len(lis)
en=en-num
for i in range(num):
	print(lis[en],end="")
	en+=1
