from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, F = map(int, input().split())
points = [(0, 0)]
points_to_index = {}

def calculator(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for i in range(1, N + 1):
    x, y = map(int, input().split())
    points.append((x, y))
    points_to_index[(x, y)] = i

dist = [INF] * (N + 1)
dist[0] = 0
visited = [False] * (N + 1)
pq = []
heappush(pq, (0, 0))
while pq:
    cur_cost, cur_node = heappop(pq)
    if cur_cost > dist[cur_node]:
        continue
    visited[cur_node] = True
    x1, y1 = points[cur_node]
    if y1 >= F:
        print(round(cur_cost))
        break
    for nx in range(-2, 3):
        for ny in range(-2, 3):
            x2, y2 = x1 + nx, y1 + ny
            next_node = points_to_index.get((x2, y2))
            if not next_node:
                continue
            if visited[next_node]:
                continue
            new_cost = cur_cost + calculator(x1, y1, x2, y2)
            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heappush(pq, (new_cost, next_node))
else:
    print(-1)