from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
sx -= 1; sy -= 1; ex -= 1; ey -= 1
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
start = []
heappush(start, [0, 1, sx, sy])
visited = [[[INF] * 3 for _ in range(M)] for _ in range(N)]
visited[sx][sy][1] = 0
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
while start:
    cost, cnt, x, y = heappop(start)
    if x == ex and y == ey:
        print(cost)
        break
    if cnt % 3 == 1:
        for i in range(2,4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] != -1 and visited[nx][ny][(cnt+1)%3] > cost+matrix[nx][ny]:
                    visited[nx][ny][(cnt+1)%3] = cost+matrix[nx][ny]
                    heappush(start, [cost+matrix[nx][ny], cnt + 1, nx, ny])
    elif cnt % 3 == 2:
        for i in range(0,2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] != -1 and visited[nx][ny][(cnt+1)%3] > cost+matrix[nx][ny]:
                    visited[nx][ny][(cnt+1)%3] = cost+matrix[nx][ny]
                    heappush(start, [cost+matrix[nx][ny], cnt + 1, nx, ny])
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] != -1 and visited[nx][ny][(cnt+1)%3] > cost+matrix[nx][ny]:
                    visited[nx][ny][(cnt+1)%3] = cost+matrix[nx][ny]
                    heappush(start, [cost+matrix[nx][ny], cnt + 1, nx, ny])
else:
    print(-1)