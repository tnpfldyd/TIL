import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer = True
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or j == k or k == i:
                continue
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                answer = False
            if matrix[i][j] == matrix[i][k] + matrix[k][j]:
                visited[i][j] = 1
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt += matrix[i][j]
print(cnt//2 if answer else -1)