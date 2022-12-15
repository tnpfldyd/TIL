from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [INF] * N
dp = [0] * N
visited[1] = 0
dp[1] = 1
start = []
heappush(start, [0, 1])
while start:
    cost, node = heappop(start)
    if cost > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = cost + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
        if cost > visited[v]:
            dp[node] += dp[v]
print(dp[0])