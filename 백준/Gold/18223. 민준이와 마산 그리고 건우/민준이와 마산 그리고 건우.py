from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, P = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
def heap(s):
    start = []
    heappush(start, [0, s])
    visited = [INF] * N
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
v1 = heap(0)
v2 = heap(P-1)
print('SAVE HIM' if v1[N-1] == v1[P-1] + v2[N-1] else 'GOOD BYE')