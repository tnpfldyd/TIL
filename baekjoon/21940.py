import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = min(matrix[a][b], t)
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            T = matrix[i][k] + matrix[k][j]
            if matrix[i][j] > T:
                matrix[i][j] = T
num = int(input())
people = list(map(int, input().strip().split()))
result = []
max_load = INF
for k in range(N):
    cnt = 0
    for i in people:
        i -= 1
        if cnt < matrix[i][k] + matrix[k][i]:
            cnt = matrix[i][k] + matrix[k][i]
    if max_load > cnt:
        max_load = cnt
        result = [k+1]
    elif max_load == cnt:
        result.append(k+1)
print(*result)