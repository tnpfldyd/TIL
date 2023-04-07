from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[INF] * M for _ in range(N)]
answer = [0] * N
stack = []

for i in range(N):
    heappush(stack, (matrix[i][M-1], i, M-1, i))
    visited[i][M-1] = matrix[i][M-1]

while stack:
    c, x, y, s = heappop(stack)
    if visited[x][y] < c:
        continue
    if not y:
        answer[s] += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            nxt_cost = c + matrix[nx][ny]
            if visited[nx][ny] > c + matrix[nx][ny]:
                visited[nx][ny] = c + matrix[nx][ny]
                heappush(stack, (visited[nx][ny], nx, ny, s))

for i in range(N):
    print(answer[i])