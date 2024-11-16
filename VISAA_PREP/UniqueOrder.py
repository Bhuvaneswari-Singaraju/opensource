N = int(input())
arr = list(map(int, input().split()))
unique = set()
newarr = []
for i in arr:
    if i not in unique:
        newarr.append(i)
        unique.add(i)
print(*newarr)
