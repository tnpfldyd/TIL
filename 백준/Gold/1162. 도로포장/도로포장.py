from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, Q = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [[INF] * (Q+1) for _ in range(N)]
visited[0][0] = 0
start = []
heappush(start, [0, 0, 0])
while start:
    x, node, q = heappop(start)
    if x > visited[node][q]:
        continue
    for k, v in matrix[node]:
        nx = k + x
        if visited[v][q] > nx:
            visited[v][q] = nx
            heappush(start, [nx, v, q])
        if Q > q and visited[v][q+1] > x:
            visited[v][q+1] = x
            heappush(start, [x, v, q+1])
result = INF
for i in visited[N-1]:
    if result > i:
        result = i
print(result)