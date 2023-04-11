from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
matrix = [[0] * (M + 2)]
for _ in range(N):
    row = [0] + list(map(int, input().split())) + [0]
    matrix.append(row)
matrix.append([0] * (M + 2))
N += 2; M += 2

dist = [[INF] * M for _ in range(N)]
dist[0][0] = 0
stack = [(0, 0, 0)]
visited = [[False] * M for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
while stack:
    cost, x, y = heappop(stack)
    if visited[x][y]:
        continue
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            next_cost = max(dist[x][y], matrix[nx][ny])
            if dist[nx][ny] > next_cost:
                dist[nx][ny] = next_cost
                heappush(stack, (next_cost, nx, ny))
answer = 0
for i in range(N):
    for j in range(M):
        answer += dist[i][j] - matrix[i][j]
print(answer)