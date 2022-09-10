from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
start = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            start.append((i, j))
            visited[i][j] = 0
            while start:
                x, y = start.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            start.append((nx, ny))
            visited[i][j] = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            if visited[i][j] == 0:
                visited[i][j] = -1
for i in visited:
    print(*i)