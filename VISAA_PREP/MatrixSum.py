N = int(input())
matrix = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
rowSum = [0]*N
colSum = [0]*N
for i in range(N):
    for j in range(N):
        rowSum[i] += matrix[i][j]
        colSum[j] += matrix[i][j]
res = []
for i in range(N):
    res.append(rowSum[i] + colSum[i])
print(" ".join(map(str, res)))
