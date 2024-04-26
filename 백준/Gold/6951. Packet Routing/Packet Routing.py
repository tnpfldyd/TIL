import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, Q = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
for i in range(N):
    matrix[i][i] = 0
    
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = c
    matrix[b][a] = c
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
            
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    print(matrix[a][b])