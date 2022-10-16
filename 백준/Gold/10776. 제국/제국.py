from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
C, N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, c = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, c, b))
    matrix[b].append((t, c, a))
visited = [[INF] * C for _ in range(N)]
s, e = map(int, input().split())
s -= 1; e -= 1
visited[s][0] = 0
start = []
heappush(start, [0, 0, s])
while start:
    x, m, node = heappop(start)
    if x > visited[node][m]:
        continue
    if node == e:
        print(visited[node][m])
        break
    for k, mon, v in matrix[node]:
        nx, nm = k + x, m + mon
        if C > nm and visited[v][nm] > nx:
            for i in range(nm, C):
                if visited[v][i] > nx:
                    visited[v][i] = nx
                else:
                    break
            heappush(start, [nx, nm, v])
else:
    print(-1)