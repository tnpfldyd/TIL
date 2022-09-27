from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
time, money = map(int, input().split())
M = int(input())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, m = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((m, t, b))
    matrix[b].append((m, t, a))
visited = [INF] * N
visited[0] = 0
start = []
result = []
heappush(start, [0, 0, 0])
while start:
    mon, x, node = heappop(start)
    for k, y, v in matrix[node]:
        nx, ny = mon+k, x+y
        if nx <= money and ny <= time:
            if v == N-1:
                result.append(nx)
            else:
                heappush(start, [nx, ny, v])
if len(result) == 0:
    print(-1)
else:
    print(min(result))