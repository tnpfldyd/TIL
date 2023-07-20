from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]

stack = []
visited = [[INF] * M for _ in range(N)]
for i in range(N - 1):
    cost = 0 if matrix[i][M - 1] else 1
    heappush(stack, (cost, i, M - 1))
    visited[i][M - 1] = cost
for i in range(1, M):
    cost = 0 if matrix[0][i] else 1
    heappush(stack, (cost, 0, i))
    visited[0][i] = cost
dx, dy = [0,0,1,-1,1,1,-1,-1],[1,-1,0,0,-1,1,-1,1]

while stack:
    cost, x, y = heappop(stack)
    if visited[x][y] < cost:
        continue
    if (x and not y) or (x == N - 1 and y != M):
        print(cost)
        break
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            nxt_cost = cost if matrix[nx][ny] else cost + 1
            if visited[nx][ny] > nxt_cost:
                visited[nx][ny] = nxt_cost
                heappush(stack, (nxt_cost, nx, ny))
