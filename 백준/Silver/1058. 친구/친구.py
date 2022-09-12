import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'Y' or (matrix[i][k] == 'Y' and matrix[k][j] == 'Y'):
                visited[i][j] = 1
final = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if visited[i][j] == 1:
            cnt += 1
    if cnt > final:
        final = cnt
print(final - 1 if final > 0 else final)