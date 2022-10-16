from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[1] * M for _ in range(N)]
sx, sy, ex, ey = 0, 0, 0, 0
start = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '+':
            start.append((i, j))
            visited[i][j] = 0
        elif matrix[i][j] == 'V':
            sx, sy = i, j
        elif matrix[i][j] == 'J':
            ex, ey = i, j
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    x, y = start.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] - 1
                start.append((nx, ny))
start = []
result = sys.maxsize
s_visited = [[0] * M for _ in range(N)]
s_visited[sx][sy] = 1
heappush(start, [visited[sx][sy], sx, sy])
while start:
    t, x, y = heappop(start)
    if result > -t:
        result = -t
    if x == ex and y == ey:
        print(result)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not s_visited[nx][ny]:
                s_visited[nx][ny] = 1
                heappush(start, [visited[nx][ny], nx, ny])