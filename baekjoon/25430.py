from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
visited = {}
for i in range(N):
    visited[i] = {}
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
    visited[a][t] = INF
    visited[b][t] = INF
s, e = map(int, input().split())
s -= 1; e -= 1
start = []
visited[s][0] = 0
heappush(start, [0, 0, s])
while start:
    x, cost, node = heappop(start)
    if node == e:
        print(x)
        break
    if x > visited[node][cost]:
        continue
    for k, v in matrix[node]:
        nx = k + x
        if k > cost and visited[v][k] > nx:
            visited[v][k] = nx
            heappush(start, [nx, k, v])
else:
    print('DIGESTA')