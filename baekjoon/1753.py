from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
S = int(input()); S -= 1
matrix = [[] for _ in range(N)]
visited = [INF] * N
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a-1].append((t, b-1))
start = []
visited[S] = 0
heappush(start, [0, S])
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for T, k in matrix[node]:
        nx = x + T
        if visited[k] > nx:
            visited[k] = nx
            heappush(start, [nx, k])
for i in visited:
    if i != INF:
        print(i)
    else:
        print('INF')