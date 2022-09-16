import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, T = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = t
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], max(matrix[i][k], matrix[k][j]))
for i in range(T):
    s, e = map(int, input().split())
    s -= 1; e -= 1
    print(matrix[s][e] if matrix[s][e] != INF else -1)