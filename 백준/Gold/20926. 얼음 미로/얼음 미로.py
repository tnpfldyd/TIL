from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
M, N = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[INF] * M for _ in range(N)]
sx, sy, ex, ey = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j].isdigit():
            matrix[i][j] = int(matrix[i][j])
        elif matrix[i][j] == 'T':
            sx, sy = i, j
            matrix[i][j] = 0
        elif matrix[i][j] == 'E':
            ex, ey = i, j
start = []
dx, dy = [0,0,1,-1], [1,-1,0,0]
visited[sx][sy] = 0
heappush(start, [0, sx, sy])
while start:
    cnt, x, y = heappop(start)
    if x == ex and y == ey:
        print(cnt)
        break
    for i in range(4):
        nx, ny = x, y
        cost = 0
        while 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < M and isinstance(matrix[nx+dx[i]][ny+dy[i]], int):
            nx += dx[i]; ny += dy[i]
            cost += matrix[nx][ny]
        if 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < M and matrix[nx+dx[i]][ny+dy[i]] != 'H':
            if matrix[nx+dx[i]][ny+dy[i]] == 'E':
                nx += dx[i]; ny += dy[i]
            ncost = cnt + cost
            if visited[nx][ny] > ncost:
                visited[nx][ny] = ncost
                heappush(start, [ncost, nx, ny])
else:
    print(-1)