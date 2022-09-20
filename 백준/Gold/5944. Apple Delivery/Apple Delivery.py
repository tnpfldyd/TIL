from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
M, N, S, V1, V2 = map(int, input().split())
S -= 1; V1 -= 1; V2 -= 1
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
def heap(s):
    visited = [INF] * N
    start = []
    heappush(start, [0, s])
    visited[s] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
sst = heap(S)
v1t = heap(V1)
v2t = heap(V2)
print(min(sst[V1] + v1t[V2], sst[V2] + v2t[V1]))