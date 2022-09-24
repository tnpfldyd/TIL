from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, s, e, money = map(int, input().split())
s -= 1; e -= 1
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [INF] * N
visited[s] = 0
start = []
heappush(start, [0, s, 0])
result = INF
while start:
    x, node, m = heappop(start)
    if node == e:
        if result > visited[node]:
            result = visited[node]
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = max(k, x); nm = m + k
        if visited[v] > nx and nm <= money:
            visited[v] = nx
            heappush(start, [nx, v, nm])
print(result if result != INF else -1)