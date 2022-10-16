from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
C, N, M = int(input()), int(input()), int(input())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, c = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, c, b))
visited = [[INF] * (C+1) for _ in range(N)]
visited[0][0] = 0
start = []
heappush(start, [0, 0, 0])
while start:
    x, m, node = heappop(start)
    if x > visited[node][m]:
        continue
    if node == N-1:
        print(visited[node][m])
        break
    for k, mon, v in matrix[node]:
        nx, nm = k + x, m + mon
        if C >= nm and visited[v][nm] > nx:
            for i in range(nm, C+1):
                if visited[v][i] > nx:
                    visited[v][i] = nx
                else:
                    break
            heappush(start, [nx, nm, v])
else:
    print('-1')