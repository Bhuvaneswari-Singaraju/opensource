N = int(input())
arr = list(map(int, input().split()))
count = {}
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i, count in count.items():
    if count == 1:
        print(i)
