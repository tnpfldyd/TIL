from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
visited = [[99999999] * M for _ in range(N)]
stx, sty, enx, eny = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
start = []
stx -= 1; sty -= 1; enx -=1; eny -=1
heappush(start, [0, stx, sty])
dx, dy = [0,0,1,-1], [1,-1,0,0]
visited[stx][sty] = 0
while start:
    ex, x, y = heappop(start)
    if x == enx and y == eny:
        print(visited[x][y])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 99999999:
                if matrix[nx][ny] == '0':
                    visited[nx][ny] = ex
                    heappush(start, [ex, nx, ny])
                else:
                    visited[nx][ny] = ex+1
                    heappush(start, [ex+1, nx, ny])