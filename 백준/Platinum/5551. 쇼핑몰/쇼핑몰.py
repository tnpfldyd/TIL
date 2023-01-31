from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())
matrix = [[] for _ in range(N)]
edges = []
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
    edges.append((a, b, t))
visited = [INF] * N
start = []
for _ in range(K):
    start_node = int(input().strip())
    start_node -= 1
    visited[start_node] = 0
    heappush(start, (0, start_node))

while start:
    cost, node = heappop(start)
    if cost > visited[node]:
        continue
    for k, v in matrix[node]:
        next_cost = cost + k
        if visited[v] > next_cost:
            visited[v] = next_cost
            heappush(start, (next_cost, v))
answer = 0
for a, b, t in edges:
    cost = (visited[a] + visited[b] + t + 1) // 2
    if answer < cost:
        answer = cost
print(answer)