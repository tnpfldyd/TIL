from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
sx -= 1; sy -= 1; ex -= 1; ey -= 1
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[[-1] * M for _ in range(N)] for _ in range(2)]
start = deque()
start.append((sx, sy, 0))
visited[0][sx][sy] = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
check = set()
while start:
    x, y, cnt = start.popleft()
    if x == ex and y == ey:
        print(visited[cnt][x][y])
        break
    for i in range(4):
        nx, ny = x + dx[i]*matrix[x][y], y + dy[i]*matrix[x][y]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[cnt][nx][ny] == -1:
                visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                start.append((nx, ny, cnt))
        if not cnt:
            nx, ny = x, y
            if i < 3:
                if (nx, ny, 0) in check:
                    continue
            else:
                if (nx, ny, 1) in check:
                    continue
            while 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < M:
                nx += dx[i]; ny += dy[i]
                if visited[cnt+1][nx][ny] == -1:
                    visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                    start.append((nx,ny,cnt+1))
                    if i < 3:
                        check.add((nx, ny, 0))
                    else:
                        check.add((nx, ny, 1))
else:
    print(-1)