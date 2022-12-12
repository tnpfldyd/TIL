import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = int(input()), int(input())
matrix = [[INF] * N for _ in range(N)]
parent = [[-1] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    if matrix[a][b] > t:
        matrix[a][b] = t
for i in range(N):
    matrix[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            nx = matrix[i][k] + matrix[k][j]
            if matrix[i][j] > nx:
                matrix[i][j] = nx
                parent[i][j] = k
for i in range(N):
    for j in range(N):
        if matrix[i][j] != INF:
            print(matrix[i][j], end=' ')
        else:
            print(0, end=' ')
    print()

def trace(x, y):
    if x == y:
        return []
    z = parent[x][y]
    if z == -1:
        return [x, y]
    return trace(x, z)[:-1] + trace(z, y)
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0 or matrix[i][j] == INF:
            print(0)
            continue
        temp = trace(i, j)
        print(len(temp), end= ' ')
        for k in temp:
            print(k+1, end=' ')
        print()