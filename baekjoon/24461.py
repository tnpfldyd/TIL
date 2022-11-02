from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N = int(input().strip())
result = [0] * N
matrix = [[] for _ in range(N)]
visited = [0] * N
for i in range(N-1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
    visited[a] += 1
    visited[b] += 1
start = []
for i in range(N):
    if visited[i] == 1:
        heappush(start, i)
while start:
    x = heappop(start)
    result[x] = 1
    for i in matrix[x]:
        visited[i] -= 1
        if visited[i] == 0:
            heappush(start, i)
answer = []
for i in range(N):
    if not result[i]:
        answer.append(i)
print(*answer)
