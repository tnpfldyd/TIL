from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, V, E = map(int, input().split())
A, B = map(int, input().split())
people = list(map(int, input().split()))

matrix = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))

def dijkstra(s):
    visited = [INF] * (V + 1)
    visited[s] = 0
    pq = []
    heappush(pq, (0, s))
    while pq:
        cost, cur = heappop(pq)
        if cost > visited[cur]:
            continue
        for nc, nn in matrix[cur]:
            nxt_cost = cost + nc
            if visited[nn] > nxt_cost:
                visited[nn] = nxt_cost
                heappush(pq, (nxt_cost, nn))
    return visited
a, b = dijkstra(A), dijkstra(B)
result = 0
for p in people:
    ap, bp = a[p], b[p]
    if ap != INF and bp != INF:
        result += ap + bp
    elif ap == INF and bp == INF:
        result -= 2
    else:
        result -= 1
print(result)