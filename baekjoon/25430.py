from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
visited = [set() for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))

s, e = map(int, input().split())
s -= 1; e -= 1
start = []
heappush(start, (0, 0, s))
while start:
    x, cost, node = heappop(start)
    if node == e:
        print(x)
        break
    for k, v in matrix[node]:
        if k > cost and v not in visited[v]:
            visited[node].add(cost)
            heappush(start, (k + x, k, v))
else:
    print('DIGESTA')