import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[INF] * N for _ in range(N)]
for i in range(N):
    matrix[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = 1
    matrix[b][a] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            new_cost = matrix[i][k] + matrix[k][j]
            if matrix[i][j] > new_cost:
                matrix[i][j] = new_cost

result = INF
points = [-1, -1]
for i in range(N - 1):
    for j in range(i + 1, N):
        temp = 0
        for k in range(N):
            temp += min(matrix[i][k], matrix[j][k])
        if result > temp:
            result = temp
            points = [i + 1, j + 1]

print(*points, result * 2)