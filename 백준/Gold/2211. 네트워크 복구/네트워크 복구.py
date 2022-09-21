from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [INF] * N
visited[0] = 0
load = [0] * N
start = []
heappush(start, [0, 0])
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = k + x
        if visited[v] > nx:
            visited[v] = nx
            load[v] = node
            heappush(start, [nx, v])
print(N-1)
for i in range(1, N):
    print(i+1, load[i]+1)