from heapq import heappop, heappush
import sys
INF = sys.maxsize
N, M = int(input()), int(input())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((cost, b))
visited = [INF] * N
start, end = map(int, input().split())
start -= 1; end -= 1
visited[start] = 0

heap = []
heappush(heap, (0, start))
while heap:
    cost, node = heappop(heap)
    if cost > visited[node]:
        continue
    for k, v in matrix[node]:
        next_cost = cost + k
        if visited[v] > next_cost:
            visited[v] = next_cost
            heappush(heap, (next_cost, v))
print(visited[end])