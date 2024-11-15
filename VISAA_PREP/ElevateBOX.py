N = int(input())
arr = list(map(int, input().split()))
B = []
for i in range(N):
    left = sum(arr[:i])
    right = sum(arr[i+1:])
    balance = abs(left - right)
    B.append(balance)
for j in B:
    print(j, end = " ")
