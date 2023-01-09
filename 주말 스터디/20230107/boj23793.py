from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
x, y, z = map(int, input().split())
x -= 1; y -= 1; z -= 1
def heap(s):
    start = []
    heappush(start, [0, s])
    visited = [INF] * N
    visited[s] = 0
    while start:
        time, node = heappop(start)
        if time > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = time + k
            if visited[v] > nx and v != y:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
def heap2(s):
    start = []
    heappush(start, [0, s])
    visited = [INF] * N
    visited[s] = 0
    while start:
        time, node = heappop(start)
        if time > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = time + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    return visited
dx = heap(x)
dx2 = heap2(x)
dy = heap(y)
if dx2[y] + dy[z] >= INF:
    print(-1, end = ' ')
else:
    print(dx2[y]+dy[z], end = ' ')
if dx[z] == INF:
    print(-1)
else:
    print(dx[z])