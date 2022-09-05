from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
sx, sy = map(int, input().split())
sx -= 1; sy -= 1
ex, ey = map(int, input().split())
ex -= 1; ey -= 1
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx, dy = [0,0,-1,1],[1,-1,0,0]
start = deque()
start.append((sx, sy, 0))
visited[sx][sy][0] = 1
while start:
    x, y, z = start.popleft()
    if x == ex and y == ey:
        print(visited[x][y][z] - 1)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if z == 0 and matrix[nx][ny] == 1 and visited[nx][ny][z] == 0:
                visited[nx][ny][1] = visited[x][y][z] + 1
                start.append((nx, ny, 1))
            elif matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
else:
    print(-1)