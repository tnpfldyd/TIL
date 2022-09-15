import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = t
    matrix[b][a] = t
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
min_sum = [INF, 0]
for i in range(N):
    if min_sum[0] > sum(matrix[i]):
        min_sum[0] = sum(matrix[i]); min_sum[1] = i + 1
print(min_sum[1])