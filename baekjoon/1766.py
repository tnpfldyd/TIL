from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
result = []
matrix = [[] for _ in range(N)]
visited = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    visited[b] += 1
start = []
for i in range(N):
    if not visited[i]:
        heappush(start, i)
while start:
    x = heappop(start)
    result.append(x + 1)
    for i in matrix[x]:
        visited[i] -= 1
        if visited[i] == 0:
            heappush(start, i)
print(*result)