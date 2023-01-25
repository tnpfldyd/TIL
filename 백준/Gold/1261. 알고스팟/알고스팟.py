from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
M, N = map(int, input().split())

matrix = [list(input().strip()) for _ in range(N)]

visited = [[INF] * M for _ in range(N)]
visited[0][0] = 0

start = []
heappush(start, (0, 0, 0))
dx, dy = [0,0,1,-1],[1,-1,0,0]
while start:
    cnt, x, y = heappop(start)
    if (x, y) == (N-1, M-1):
        print(cnt)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            next_cost = cnt
            if matrix[nx][ny] == '1':
                next_cost = cnt + 1
            if visited[nx][ny] > next_cost:
                visited[nx][ny] = next_cost
                heappush(start, (next_cost, nx, ny))