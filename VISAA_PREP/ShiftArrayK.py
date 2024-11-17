N = int(input())
arr = list(map(int, input().split()))
k = int(input())
k%=N
arr = arr[-k:] + arr[:-k]
print(*arr)
