import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
matrix = [[0] * N for _ in range(N)]
for i in range(N):
    matrix[i][i] = 1
    
for _ in range(M):
    a, b = map(int, input().split())
    matrix[b - 1][a - 1] = 1
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

result = 0
for i in range(N):
    temp = 0
    for j in range(N):
        if i == j:
            continue
        if matrix[i][j] or matrix[j][i]:
            temp += 1

    if temp == N - 1:
        result += 1

print(result)