from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, K = map(int, input().split())
matrix = [[] for _ in range(N+2)]
for _ in range(K):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [INF] * (N+2)
visited[0] = 0
start = []
heappush(start, (0, 0, 100))
while start:
    cost, node, oil = heappop(start)
    if cost > visited[node]:
        continue
    for k, v in matrix[node]:
        if k > 100:
            continue
        new_cost = cost + k
        if oil >= k:
            new_oil = oil - k
        else:
            new_oil = 100 - k
            new_cost += 5
        if visited[v] > new_cost:
            visited[v] = new_cost
            heappush(start, (new_cost, v, new_oil))
print(visited[N+1])