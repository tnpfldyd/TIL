from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
S, E = map(int, input().split())

matrix = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((-t, b))
    matrix[b].append((-t, a))

visited = [INF] * (N + 1)
visited[S] = -INF
pq = []
heappush(pq, (-INF, S))

while pq:
    cost, x = heappop(pq)
    if x == E:
        print(-cost)
        break
    if cost > visited[x]:
        continue
    for nc, nn in matrix[x]:
        next_c = max(cost, nc)
        if visited[nn] > next_c:
            visited[nn] = next_c
            heappush(pq, (next_c, nn))
else:
    print(0)