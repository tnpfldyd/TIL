from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [False] * N
start = []
cnt = 0; temp = 0
heappush(start, [0, 0])
while start:
    x, node = heappop(start)
    if temp == N:
        break
    if not visited[node]:
        visited[node] = True
        temp += 1
        cnt += x
        for k, v in matrix[node]:
            heappush(start, [k, v])
print(cnt)