import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, T = map(int, input().split())
matrix = [[INF] * M for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = t
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or k == j:
                continue
            new = max(matrix[i][k],matrix[k][j])
            if matrix[i][j] > new:
                matrix[i][j] = new
for i in range(T):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    print(matrix[a][b] if matrix[a][b] != INF else -1)