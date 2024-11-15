N = int(input())
matrix = []
for i in range(N):
    arr = list(map(int, input().split()))
    matrix.append(arr)
for i in range(N):
    for j in range(N//2):
        matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1],matrix[i][j]
        
for arr in matrix:
    print(" ".join(map(str, arr)))
