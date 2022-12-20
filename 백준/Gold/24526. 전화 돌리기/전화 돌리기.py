from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
in_degree = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[b].append(a)
    in_degree[a] += 1
start = []
result = 0
for i in range(N):
    if not in_degree[i]:
        heappush(start, i)
        result += 1
while start:
    x = heappop(start)
    for i in matrix[x]:
        in_degree[i] -= 1
        if not in_degree[i]:
            heappush(start, i)
            result += 1
print(result)