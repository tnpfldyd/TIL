from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
# sx, sy = 0, 0
start = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            start.append((i, j))
            # sx, sy = i, j
visited = [[0] * M for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
while start:
    x, y = start.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                start.append((nx, ny))
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
for visit in visited:
    print(*visit)