from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = int(input()), int(input())
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]
degree = [0] * N
parent = [0] * N
visited = [0] * N
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    rev_matrix[b].append((t, a))
    degree[b] += 1
start = []
heappush(start, 0)
while start:
    node = heappop(start)
    if not node and not degree[0]:
        break
    for k, v in matrix[node]:
        degree[v] -= 1
        nx = visited[node] + k
        if nx > visited[v]:
            visited[v] = nx
            parent[v] = node
        if not degree[v]:
            heappush(start, v)
print(visited[0])
result = [1]
start = parent[0]
result.append(start+1)
while start != 0:
    start = parent[start]
    result.append(start+1)
print(*result[::-1])