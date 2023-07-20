from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())
X -= 1

matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))

visited = [INF] * N
visited[X] = 0
pq = []
heappush(pq, (0, X))
while pq:
    cost, x = heappop(pq)
    if visited[x] < cost:
        continue
    for nxt_c, nxt_n in matrix[x]:
        new_c = nxt_c + cost
        if visited[nxt_n] > new_c:
            visited[nxt_n] = new_c
            heappush(pq, (new_c,  nxt_n))

answer = max(visited) * 2
print(answer)