import math
nrr=int(input())
ans=math.sin(math.radians(nrr))
if ans<1:
	print(round(ans,1))
else:
	print(round(ans))
