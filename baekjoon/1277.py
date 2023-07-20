from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, W = map(int, input().split())
M = float(input())

v = [tuple(map(int, input().split())) for _ in range(N)]
matrix = [[INF] * N for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        x, y = v[i][0] - v[j][0], v[i][1] - v[j][1]
        dist = (x * x + y * y) ** 0.5
        if dist <= M:
            matrix[i][j] = matrix[j][i] = dist
        else:
            matrix[i][j] = matrix[j][i] = INF
        
for _ in range(W):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a][b] = matrix[b][a] = 0

visited = [INF] * N
visited[0] = 0
pq = []
heappush(pq, (0, 0))
while pq:
    cost, now = heappop(pq)
    if cost > visited[now]:
        continue
    for i in range(N):
        if matrix[now][i] == INF:
            continue
        nc = cost + matrix[now][i]
        if nc < visited[i]:
            visited[i] = nc
            heappush(pq, (nc, i))

print(int(visited[N - 1] * 1000))