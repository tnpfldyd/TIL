from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
visited = [[INF] * N for _ in range(2)]
for _ in range(M):
    a, b, t, d = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b, d))
    matrix[b].append((t, a, d))
start = []
heappush(start, [0, 0, 0])
visited[0][0] = 0

while start:
    x, node, don = heappop(start)
    if x > visited[don][node]:
        continue
    for k, v, d in matrix[node]:
        nx = x + k
        if visited[don][v] > nx:
            visited[don][v] = nx
            heappush(start, [nx, v, don])
        if not don:
            nx = x + k - d
            if visited[1][v] > nx:
                visited[1][v] = nx
                heappush(start, [nx, v, don+1])
for idx, cost in enumerate(visited[1]):
    if not idx:
        continue
    print(cost)