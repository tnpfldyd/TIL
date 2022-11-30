from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, A, S, E = map(int, input().split())
matrix = [[] for _ in range(N)]
air = {}
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
def heap(S):
    start = []
    heappush(start, [0, S])
    visited = [INF] * N
    visited[S] = 0
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
answer = heap(S)[E]
for _ in range(A):
    a, b = map(int, input().split())
    answer = min(answer, heap(S)[a] + heap(b)[E])
print(answer)