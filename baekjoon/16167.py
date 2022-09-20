from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d, t = map(int, input().split())
    a -= 1; b -= 1
    if t > 10:
        matrix[a].append((c + ((t - 10) * d), b))
    else:
        matrix[a].append((c, b))
start = []
heappush(start, [0, 0, [1]])
visited = [INF] * N
visited[0] = 0
result = []
while start:
    x, node, load = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v, load+[v+1]])
            if v == N-1:
                result.append((visited[v], load + [v+1]))
        elif visited[v] == nx and v == N-1:
            result.append((visited[v], load + [v+1]))
result = sorted(result, key = lambda x : (x[0], len(x[1])))
if visited[N-1] == INF:
    print('It is not a great way.')
else:
    print(visited[N-1], len(result[0][1]))