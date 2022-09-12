import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[INF] * (N)  for _ in range(N)]
for i in range(M):
    a, b, cost = map(int, input().split())
    matrix[a-1][b-1] = cost
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
result = INF
for i in range(N):
    if result > matrix[i][i] :
        result = matrix[i][i]
print(result if result != INF else -1)