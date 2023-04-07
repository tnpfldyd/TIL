from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
edges = []
matrix = [[] for _ in range(N)]
result = 0
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
    edges.append((a, b))
    result += t

def dijkstra(s):
    stack = [(0, s)]
    visited = [INF] * N
    visited[s] = 0
    while stack:
        cur_cost, cur_node = heappop(stack)
        if visited[cur_node] < cur_cost:
            continue
        for nxt_cost, nxt_node in matrix[cur_node]:
            res_cost = cur_cost + nxt_cost
            if visited[nxt_node] > res_cost:
                visited[nxt_node] = res_cost
                heappush(stack, (res_cost, nxt_node))
    return visited

S, T = map(int, input().split())
S -= 1; T -= 1
min_cost = INF
costS, costT = dijkstra(S), dijkstra(T)
for edge in edges:
    a, b = edge
    min_cost = min(min_cost, costS[a] + costT[b], costT[a] + costS[b])
result -= min_cost

print(result)