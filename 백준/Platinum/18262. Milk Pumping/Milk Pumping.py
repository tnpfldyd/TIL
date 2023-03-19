from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost, flow = map(int, input().split())
    matrix[a].append((cost, b, flow))
    matrix[b].append((cost, a, flow))

stack = []
visited = [-INF] * (N + 1)

heappush(stack, (0, 1, 1000))

while stack:
    cost, node, flow = heappop(stack)
    for next_cost, next_node, next_flow in matrix[node]:
        new_flow = min(flow, next_flow)
        new_cost = cost + next_cost
        if visited[next_node] < new_flow / new_cost:
            visited[next_node] = new_flow / new_cost
            heappush(stack, (new_cost, next_node, new_flow))
print(int(visited[N] * 1e6))