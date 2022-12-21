from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split()) # N 노드의 갯수 M 간선의 갯수
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [INF] * N
visited[0] = 0
start = []
heappush(start, [0, 0])
while start:
    cost, node = heappop(start)
    if cost > visited[node]:
        continue
    for next_cost, next_node in matrix[node]:
        nx = cost + next_cost
        if visited[next_node] > nx:
            visited[next_node] = nx
            heappush(start, [nx, next_node])