import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
matrix2 = [list(input().strip()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            matrix[i][j] = 0
            matrix2[i][j] = 0
        else:
            if matrix[i][j] == '.':
                matrix[i][j] = INF
                matrix2[i][j] = INF
            else:
                matrix[i][j] = int(matrix[i][j])
                matrix2[i][j] = int(matrix2[i][j])
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
            matrix2[i][j] = min(matrix2[i][j],matrix2[i][k] + matrix2[k][j])
print(matrix)
print(matrix2)