from heapq import heappop, heappush
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
INF = sys.maxsize

N, M, A, B = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

pq = []
dist = [INF] * (N + 1)
heappush(pq, (0, A))
dist[A] = 0
prev = [[] for _ in range(N + 1)]

while pq:
    cur_cost, cur_node = heappop(pq)
    if cur_cost > dist[cur_node]:
        continue

    for nxt_node, nxt_cost in graph[cur_node]:
        distance = cur_cost + nxt_cost
        if dist[nxt_node] > distance:
            dist[nxt_node] = distance
            prev[nxt_node] = [cur_node]
            heappush(pq, (distance, nxt_node))

        elif dist[nxt_node] == distance:
            prev[nxt_node].append(cur_node)

result = set()

def get_paths(node):
    result.add(node)
    if node == A:
        return
    for p in prev[node]:
        get_paths(p)

get_paths(B)
result = sorted(set(result))
print(len(result))
print(*result)