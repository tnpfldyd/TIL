from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[b].append((t, a))
k_list = list(map(int, input().rstrip().split()))
start = []
visited = [INF] * N
for i in k_list:
    i -= 1
    visited[i] = 0
    heappush(start, [0, i])
while start:
    x, node = heappop(start)
    if x > visited[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if visited[v] > nx:
            visited[v] = nx
            heappush(start, [nx, v])
num = 0
result = 0
for i in range(N):
    if visited[i] > result:
        result = visited[i]
        num = i+1
print(num)
print(result)