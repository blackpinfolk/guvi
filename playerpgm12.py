ar,k=list(map(int,input().split()))
arr=input().split()
print(*arr[-k:]+arr[:-k])
