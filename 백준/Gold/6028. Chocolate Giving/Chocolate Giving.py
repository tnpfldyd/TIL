from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, Q = map(int, input().split())
matrix = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    matrix[a].append((c, b))
    matrix[b].append((c, a))
    
def dijkstra(x):
    visited = [INF] * (N + 1)
    visited[x] = 0
    pq = []
    heappush(pq, (0, x))
    while pq:
        cur_c, cur_x = heappop(pq)
        if visited[cur_x] < cur_c:
            continue
        for nxt_c, nxt_x in matrix[cur_x]:
            nc = cur_c + nxt_c
            if visited[nxt_x] > nc:
                visited[nxt_x] = nc
                heappush(pq, (nc, nxt_x))
    return visited

visit = dijkstra(1)
for _ in range(Q):
    a, b = map(int, input().split())
    answer = visit[a] + visit[b]
    print(answer)