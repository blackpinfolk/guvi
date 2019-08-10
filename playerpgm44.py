arr,k=input().split()
arr=list(map(str,arr))
k=int(k)
print(*arr[-k:]+arr[:-k],sep="")
