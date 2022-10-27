from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, S, E = map(int, input().split())
S -= 1; E -= 1
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
start = []
heappush(start, [0, S])
visited = [INF] * N
load = [0] * N
visited[S] = 0
load[S] = 1
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            load[v] = load[node]
            heappush(start, [nx, v])
        elif visited[v] == nx:
            load[v] = (load[v] + load[node]) % 1000000009
print(load[E])
