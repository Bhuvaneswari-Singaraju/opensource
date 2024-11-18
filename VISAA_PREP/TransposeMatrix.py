N = int(input())
matrix = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
transpose = []
for i in range(N):
    rowT = []
    for j in range(N):
        rowT.append(matrix[j][i])
    transpose.append(rowT)
for i in transpose:
    print(' '.join(map(str, i)))
