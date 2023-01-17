from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
start = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            start.append((i, j))
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    x, y = start.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not matrix[nx][ny]:
            matrix[nx][ny] = matrix[x][y] + 1
            start.append((nx, ny))
flag = False
max_cnt = 0
for i in range(N):
    for j in range(M):
        if not matrix[i][j]:
            flag = True
        max_cnt = max(max_cnt, matrix[i][j])
if flag:
    print(-1)
else:
    print(max_cnt - 1)