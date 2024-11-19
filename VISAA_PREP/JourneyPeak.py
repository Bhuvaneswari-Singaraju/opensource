N =int(input())
arr = list(map(int, input().split()))
res = 0
maxRes = 0
for i in arr:
    res += i
    maxRes = max(maxRes, res)
print(maxRes)
