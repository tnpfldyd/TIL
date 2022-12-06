from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, T, ex, ey = map(int, input().split())
ex -= 1; ey -= 1
matrix = [list(input().strip()) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
visited = [[[INF] * 2 for _ in range(N)] for _ in range(N)]
visited[0][0][0] = 0
start = []
heappush(start, [0, 0, 0, 0])
while start:
    cost, x, y, trans = heappop(start)
    if x == ex and y == ey:
        print(cost)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny][0] > cost + 1:
            visited[nx][ny][0] = cost + 1
            heappush(start, [cost+1, nx, ny, 0])
    if not trans and visited[x][y][1] > cost + T:
        visited[x][y][1] = cost + T
        heappush(start, [cost+T, x, y, 1])
    if trans:
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < N and matrix[nx+dx[i]][ny+dy[i]] == '.':
                nx += dx[i]; ny += dy[i]
            if 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < N and matrix[nx+dx[i]][ny+dy[i]] == '#':
                nx += dx[i]; ny += dy[i]
                if visited[nx][ny][1] > cost + 1:
                    visited[nx][ny][1] = cost + 1
                    heappush(start, [cost+1, nx, ny, 1])