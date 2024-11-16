T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    rem = (X+1)-Y
    print(rem)
