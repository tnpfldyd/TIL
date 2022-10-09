from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input()); M = int(input())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    if a == b:
        continue
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
visited = [False] * N
start = []
heappush(start, [0, 0])
cnt = 0; temp = 0
while start:
    x, node = heappop(start)
    if temp == N:
        break
    if not visited[node]:
        visited[node] = True
        temp += 1
        cnt += x
        for k, v in matrix[node]:
            heappush(start, (k, v))
print(cnt)