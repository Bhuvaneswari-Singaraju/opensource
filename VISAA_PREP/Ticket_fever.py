T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    num = N-M
    if num > 0:
        print(num)
    else:
        print("0")
