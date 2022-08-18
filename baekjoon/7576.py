from pprint import pprint
from collections import deque
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
start = deque()
dx, dy = [0, 1, 0, -1],[-1, 0, 1, 0]
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 1:
            start.append((i, j))
            visited[i][j] = 1
        if matrix[i][j] == -1:
            visited[i][j] = -1
while start:
    x, y = start.popleft()
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
cnt = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            cnt += 1
pprint(visited)
print(max(map(max, visited)) - 1 if cnt == 0 else -1)