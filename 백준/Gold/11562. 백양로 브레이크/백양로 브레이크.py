import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    if t == 1:
        matrix[a][b] = 0
        matrix[b][a] = 0
    else:
        matrix[a][b] = 0
        matrix[b][a] = 1
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    print(matrix[a][b])