from heapq import heappop, heappush
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b, i))
    matrix[b].append((t, a, i))
def heap(edge):
    start = []
    heappush(start, [0, 0])
    visited = [INF] * N
    visited[0] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v, l in matrix[node]:
            nx = x + k
            if l != edge and visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
edges = set()
visited = heap(-1)
start = deque()
start.append(N-1)
while start:
    x = start.popleft()
    if x == 0:
        continue
    for k, v, l in matrix[x]:
        if visited[x] - k == visited[v] and l not in edges:
            start.append(v)
            edges.add(l)
max_cnt = 0
for i in edges:
    temp = heap(i)
    if max_cnt < temp[N-1]:
        max_cnt = temp[N-1]
if max_cnt == INF:
    print(-1)
else:
    print(max_cnt - visited[N-1])