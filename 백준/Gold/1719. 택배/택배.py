import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
result = [['-'] * N for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = t
    matrix[b][a] = t
    result[a][b] = b + 1
    result[b][a] = a + 1
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
                result[i][j] = result[i][k]
for i in result:
    print(*i)