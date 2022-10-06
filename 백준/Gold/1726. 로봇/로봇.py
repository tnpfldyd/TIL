from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sx -= 1; sy -= 1; sd -= 1; ex -= 1; ey -= 1; ed -= 1
dx, dy = [0,0,1,-1], [1,-1,0,0]
visited = [[[-1] * 4 for _ in range(M)] for _ in range(N)]
visited[sx][sy][sd] = 0
start = deque()
start.append((sx, sy, sd))
while start:
    x, y, d = start.popleft()
    if x == ex and y == ey and d == ed:
        print(visited[x][y][d])
        break
    for i in range(1, 4):
        nx, ny = x + (dx[d] * i), y + (dy[d] * i)
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        if matrix[nx][ny] == 1:
            break
        if visited[nx][ny][d] == -1:
            visited[nx][ny][d] = visited[x][y][d] + 1
            start.append((nx, ny, d))
    if d > 1:
        for i in range(2):
            if visited[x][y][i] == -1:
                visited[x][y][i] = visited[x][y][d] + 1
                start.append((x, y, i))
    if d <= 1:
        for i in range(2,4):
            if visited[x][y][i] == -1:
                visited[x][y][i] = visited[x][y][d] + 1
                start.append((x, y, i))