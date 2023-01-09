from heapq import heappop, heappush
import sys
INF = sys.maxsize
def dijkstra(sn, n, matrix):
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
def solution(n, s, a, b, fares):
    s -= 1; a -= 1; b -= 1
    matrix = [[] for _ in range(n)]
    for x, y, cost in fares:
        x -= 1; y -= 1
        matrix[x].append((cost, y))
        matrix[y].append((cost, x))
    answer = INF
    svisit, avisit, bvisit = dijkstra(s, n, matrix), dijkstra(a, n, matrix), dijkstra(b, n, matrix)
    for i in range(n):
        answer = min(answer, svisit[i] + avisit[i] + bvisit[i])
    return answer