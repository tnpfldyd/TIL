from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
node_cost = list(map(int, input().strip().split()))
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [[INF] * (max(node_cost)+1) for _ in range(N)]
visited[0][node_cost[0]] = 0
start = []
real_visited = [[False] * (max(node_cost)+1) for _ in range(N)]
real_visited[0][node_cost[0]] = True
heappush(start, [0, node_cost[0], 0])
while start:
    x, cost, node = heappop(start)
    x = -x
    if node == N-1:
        print(x)
        break
    if visited[node][cost] < x:
        continue
    for k, v in matrix[node]:
        nx = cost * k + x
        if not real_visited[v][cost]:
            visited[v][cost] = nx
            real_visited[v][cost] = True
            heappush(start, [-nx, min(cost, node_cost[v]), v])