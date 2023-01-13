from heapq import heappop, heappush
import sys
INF = sys.maxsize
n, s, a, b = 6, 4, 6 ,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
s -= 1; a -= 1; b -= 1
matrix = [[] for _ in range(n)]
for x, y, cost in fares:
    x -= 1; y -= 1
    matrix[x].append((cost, y))
    matrix[y].append((cost, x))

def dijkstra(sn):
    start = []
    heappush(start, (0, sn))
    visited = [INF] * n
    visited[sn] = 0
    while start:
        cost, node = heappop(start)
        if cost > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = cost + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, (nx, v))
    return visited
answer = INF
svisit, avisit, bvisit = dijkstra(s), dijkstra(a), dijkstra(b)
for i in range(n):
    answer = min(answer, svisit[i] + avisit[i] + bvisit[i])
print(answer)