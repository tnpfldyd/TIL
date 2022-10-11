from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((-t, b))
    matrix[b].append((-t, a))
visited = [INF] * N
start = []
s, e = map(int, input().split())
s -= 1; e -= 1
visited[s] = 0
heappush(start, [-1000000001, s])
while start:
    x, node = heappop(start)
    if visited[node] < x:
        continue
    for k, v in matrix[node]:
        nx = max(x, k)
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
print(-visited[e])