from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
left, right = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
start = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            start.append((i, j, left, right))
            visited[i][j] = True
cnt = 1
dx, dy = [1,-1,0,0],[0,0,1,-1]
while start:
    x, y, l, r = start.popleft()
    for i in range(2):
        nx, ny = x, y
        while 0 <= nx + dx[i] < N and matrix[nx + dx[i]][ny] != 1:
            nx += dx[i]
            if not visited[nx][ny]:
                visited[nx][ny] = True
                start.append((nx, ny, l, r))
                cnt += 1
    for i in range(2, 4):
        nx, ny = x, y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if i == 2 and r:
                if not visited[nx][ny] and matrix[nx][ny] != 1:
                    visited[nx][ny] = True
                    cnt += 1
                    start.append((nx, ny, l, r-1))
            elif i == 3 and l:
                if not visited[nx][ny] and matrix[nx][ny] != 1:
                    visited[nx][ny] = True
                    cnt += 1
                    start.append((nx, ny, l-1, r))
print(cnt)