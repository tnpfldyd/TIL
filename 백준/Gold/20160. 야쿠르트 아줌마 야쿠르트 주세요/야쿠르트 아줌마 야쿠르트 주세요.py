from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

def dijkstra(s):
    visited = [INF] * (V + 1)
    visited[s] = 0
    pq = []
    heappush(pq, (0, s))
    while pq:
        cur_cost, cur_node = heappop(pq)
        if cur_cost > visited[cur_node]:
            continue
        for nxt_cost, nxt_node in graph[cur_node]:
            temp = cur_cost + nxt_cost
            if visited[nxt_node] > temp:
                visited[nxt_node] = temp
                heappush(pq, (temp, nxt_node))
    
    return visited

points = list(map(int, input().split()))
start = int(input())
result = dijkstra(start)
total = 0
answer = INF
cur_point = points[0]

for point in points:
    temp = dijkstra(cur_point)[point]
    if temp == INF: 
        continue
    total += temp
    cur_point = point
    if total >= result[point]:
        answer = min(answer, point)

print(answer if answer != INF else -1)