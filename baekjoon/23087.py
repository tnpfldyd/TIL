from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M, s, e = map(int, input().split())
s -= 1; e -= 1
matrix = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b, str(i)))
visited = [INF] * N
visited[s] = 0
start = []
heappush(start, [0, s, ''])
result = set()
while start:
    x, node, cnt = heappop(start)
    if x > visited[node]:
        continue
    for k, v, l in matrix[node]:
        nx = k + x
        if v == e:
            result.add((nx, cnt+l))
        if visited[v] >= nx:
            visited[v] = nx
            heappush(start, [nx, v, cnt+l])
if visited[e] == INF:
    print("-1")
else:
    print(visited[e])
    min_cnt = INF
    for k, v in result:
        if k == visited[e] and min_cnt > len(v):
            min_cnt = len(v)
    print(min_cnt)
    final = 0
    for k, v in result:
        if k == visited[e] and min_cnt == len(v):
            final += 1
    final %= (1000000000+9)
    print(final)