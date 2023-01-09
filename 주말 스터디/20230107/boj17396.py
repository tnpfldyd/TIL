from heapq import heappop, heappush
import sys
INF = sys.maxsize
N, M = map(int, input().split())
qnsrl = list(map(int, input().rstrip().split()))
qnsrl[-1] = 0
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
start = []
heappush(start, [0, 0])
visited = [INF]*N
visited[0] = 0
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx and qnsrl[v] != 1:
            visited[v] = nx
            heappush(start, [nx, v])
print(visited[-1] if visited[-1] != INF else -1)