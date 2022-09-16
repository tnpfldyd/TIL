from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M, T, S = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
start = []
heappush(start, [0, S])
visited = [INF] * N
visited[S] = 0
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
for i in range(N):
    if visited[i] > T/2:
        print(-1)
        break
else:
    visited.sort()
    cnt = 0
    result = 1
    for i in range(N):
        if cnt + visited[i] > T/2:
            result += 1
            cnt = visited[i]
        else:
            cnt += visited[i]
    print(result)