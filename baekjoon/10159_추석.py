import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
matrix = [[0] * (N)  for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1
for i in range(N):
    cnt = 0
    for j in range(N):
        cnt += matrix[i][j] + matrix[j][i]
    print(N - 1 - cnt)