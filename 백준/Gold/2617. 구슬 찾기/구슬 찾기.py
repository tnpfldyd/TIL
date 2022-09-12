import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[0] * N for _ in range(N)]
matrix2 = [[0] * N for _ in range(N)] 
for i in range(M):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix2[b-1][a-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1
            if matrix2[i][j] == 1 or (matrix2[i][k] == 1 and matrix2[k][j] == 1):
                matrix2[i][j] = 1
final = 0
for i in range(N):
    cnt = 0
    cnt2 = 0
    for j in range(N):
        if matrix[i][j] == 1:
            cnt += 1
        if matrix2[i][j] == 1:
            cnt2 += 1
    if cnt >= (N - (N//2)):
        final += 1
    if cnt2 >= (N - (N//2)):
        final += 1
print(final)