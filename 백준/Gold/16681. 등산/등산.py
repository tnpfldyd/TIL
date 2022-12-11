from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, D, E = map(int, input().split())
height_list = list(map(int, input().strip().split()))
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [[INF] * 2 for _ in range(N)]
visited[0][0] = 0; visited[N-1][1] = 0
start = []
heappush(start, [0, 0, 0]); heappush(start, [0, N-1, 1])
while start:
    cost, node, dir = heappop(start)
    if cost > visited[node][dir]:
        continue
    for k, v in matrix[node]:
        nx = cost + k
        if visited[v][dir] > nx and height_list[v] > height_list[node]:
            visited[v][dir] = nx
            heappush(start, [nx, v, dir])
result = -INF
for i in range(N):
    if visited[i][0] == INF or visited[i][1] == INF:
        continue
    temp = E * height_list[i] - D * (visited[i][0] + visited[i][1])
    if result < temp:
        result = temp
print(result if result != -INF else 'Impossible')