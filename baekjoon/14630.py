from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
nodes = []
for _ in range(N):
    node = input().strip()
    nodes.append(node)
matrix = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        t = 0
        for k in range(len(nodes[0])):
            t += (int(nodes[i][k]) - int(nodes[j][k])) ** 2
        matrix[i].append((t, j))
        matrix[j].append((t, i))
s, e = map(int, input().split())
s -= 1; e -= 1
start = []
heappush(start, [0, s])
visited = [INF] * N
visited[s] = 0
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
print(visited[e])
