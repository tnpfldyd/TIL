from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())
matrix = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))

visited = [INF] * (N + 1)
visited[N] = 0
stack = []
heappush(stack, (0, N))

while stack:
    cost, cur = heappop(stack)
    if visited[cur] < cost:
        continue
    for next_cost, next_node in matrix[cur]:
        nx = next_cost + cost
        if visited[next_node] > nx:
            visited[next_node] = nx
            heappush(stack, (nx, next_node))

pasture = [INF] * (N + 1)
for _ in range(K):
    a, b = map(int, input().split())
    nx = visited[a] - b
    if pasture[a] < nx:
        continue
    pasture[a] = nx
    heappush(stack, (nx, a))

answer = [0] * (N + 1)
while stack:
    cost, cur = heappop(stack)
    if pasture[cur] < cost:
        continue
    if cost <= visited[cur]:
        answer[cur] = 1
    for next_cost, next_node in matrix[cur]:
        nx = next_cost + cost
        if pasture[next_node] > nx:
            pasture[next_node] = nx
            heappush(stack, (nx, next_node))

for i in range(1, N):
    print(answer[i])
