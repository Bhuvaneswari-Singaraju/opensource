N = int(input())
for i in range(1, N+1):
    first = ''.join(str(j) for j in range(1, i+1))
    second = ''.join(str(j) for j in range(i, 0, -1))
    space = " "*(2*(N-i))
    print(first + space + second)
