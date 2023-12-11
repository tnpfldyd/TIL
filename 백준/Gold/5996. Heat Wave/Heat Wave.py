from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, S, E = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    matrix[a].append((c, b))
    matrix[b].append((c, a))

pq = []
visited = [INF] * (N + 1)
visited[S] = 0
heappush(pq, (0, S))

while pq:
    cost, cur = heappop(pq)
    if cur == E:
        print(cost)
        break
    if cost > visited[cur]:
        continue
    for nxt_cost, nxt_node in matrix[cur]:
        temp = cost + nxt_cost
        if visited[nxt_node] > temp:
            visited[nxt_node] = temp
            heappush(pq, (temp, nxt_node))