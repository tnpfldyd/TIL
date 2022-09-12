import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[0] * (N)  for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    if matrix[x][y] == 1 and matrix[y][x] == 0:
        print(-1)
    elif matrix[x][y] == 0 and matrix[y][x] == 1:
        print(1)
    else:
        print(0)