import sys
input = sys.stdin.readline
INF = sys.maxsize
T = int(input())
matrix = [[INF] * (T) for _ in range(T)]
M = int(input())
for i in range(M):
    x, y, k = map(int, input().split())
    matrix[x-1][y-1] = min(matrix[x-1][y-1], k)
for i in range(T):
    matrix[i][i] = 0
for k in range(T):
    for a in range(T):
        for b in range(T):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])
for i in range(T):
    for j in range(T):
        if matrix[i][j] == INF:
            matrix[i][j] = 0
for i in matrix:
    print(*i)