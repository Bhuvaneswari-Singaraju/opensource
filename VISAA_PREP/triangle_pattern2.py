N = int(input())
num = 1
for i in range(1, N+1):
    for j in range(i):
        print(i, end = " ")
        num += 1
    print()
