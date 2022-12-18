from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
cost_list = list(map(int, input().strip().split()))
matrix = [[] for _ in range(N)]
for _ in range(M):
    t, a, b = map(int, input().split())
    t -= 1; a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
start = []
for idx, cost in enumerate(cost_list):
    heappush(start, [cost, idx])
while start:
    cost, node = heappop(start)
    if cost > cost_list[node]:
        continue
    for k, v in matrix[node]:
        nx = cost + cost_list[v]
        if cost_list[k] > nx:
            cost_list[k] = nx
            heappush(start, [nx, k])
print(cost_list[0])