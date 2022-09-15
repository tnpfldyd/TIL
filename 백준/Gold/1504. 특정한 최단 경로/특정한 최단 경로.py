from heapq import heappop,heappush
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
n1, n2 = map(int, input().split())
n1 -= 1; n2 -= 1
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
answer = min(heap(0)[n1] + heap(n1)[n2] + heap(n2)[N-1], heap(0)[n2] + heap(n2)[n1] + heap(n1)[N-1])
print(answer if answer < INF else -1)