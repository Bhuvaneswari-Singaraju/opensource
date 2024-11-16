T = int(input())
for i in range(1, T+1):
    X, N = map(int, input().split())
    points = X / 10
    op = points * N
    print(int(op))
