n = int(input())
arr = list(map(int, input().split()))
x = int(input())
Index = -1
for i in range(0,n):
    if arr[i] == x:
        Index = i
        break
print(Index)
