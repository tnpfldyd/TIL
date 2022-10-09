from heapq import heappop, heappush
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
K_list = list(map(int, input().rstrip().split()))
matrix = [[] for _ in range(N+1)]
start = []
for _ in range(M):
    a, b, t = map(int, input().split())
    matrix[a].append((t, b))
    matrix[b].append((t, a))
for i in K_list:
    matrix[0].append((0, i))
    heappush(start, [0, i])
visited = [False] * (N+1)
visited[0] = True
cnt, temp = 0, 0
while start:
    x, node = heappop(start)
    if temp == N:
        break
    if not visited[node]:
        cnt += x; temp += 1; visited[node] = True
        for k, v in matrix[node]:
            heappush(start, [k, v])
print(cnt)
