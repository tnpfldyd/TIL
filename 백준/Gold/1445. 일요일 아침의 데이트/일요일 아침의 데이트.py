from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M= map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
start = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'S':
            heappush(start, [0, 0, i, j])
            visited[i][j] = 0
dx, dy = [0,0,1,-1], [1,-1,0,0]
while start:
    grb, grbs, x, y = heappop(start)
    if matrix[x][y] == 'F':
        print(grb, grbs)
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
            if matrix[nx][ny] == 'g':
                visited[nx][ny] = grb
                heappush(start, [grb+1, grbs, nx, ny])
            elif matrix[nx][ny] == '.':
                cnt = 0
                for i in range(4):
                    sx, sy = nx + dx[i], ny + dy[i]
                    if 0 <= sx < N and 0 <= sy < M:
                        if matrix[sx][sy] == 'g':
                            cnt += 1
                if cnt > 0:
                    visited[nx][ny] = grb
                    heappush(start, [grb, grbs+1, nx, ny])
                else:
                    visited[nx][ny] = grb
                    heappush(start, [grb, grbs, nx, ny])
            else:
                visited[nx][ny] = grb
                heappush(start, [grb, grbs, nx, ny])