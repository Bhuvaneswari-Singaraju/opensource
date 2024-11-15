n = int(input())
arr = list(map(int, input().split()))
newarr = arr[::-1]
for i in newarr:
    print(i, end = " ")
