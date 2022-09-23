from heapq import heappop, heappush
import sys
INF = sys.maxsize
n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3, 7]
summits = [1, 5]
matrix = [[] for _ in range(n)]
for a, b, t in paths:
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [INF] * n
start = []
for i in gates:
    i -= 1
    visited[i] = 0
    heappush(start, [0, i])
while start:
    x, node = heappop(start)
    if x > visited[node] or node+1 in summits:
        continue
    for k, v in matrix[node]:
        nx = max(x, k)
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
summits.sort()
num, load = 0, INF
for i in summits:
    i -= 1
    if load > visited[i]:
        load = visited[i]
        num = i + 1
answer = []
answer.append(num); answer.append(load)
print(answer)