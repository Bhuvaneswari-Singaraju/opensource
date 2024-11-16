N = int(input())
arr = list(map(int, input().split()))
shift = 1
arr = arr[shift:] + arr[:shift]
print(*arr)
