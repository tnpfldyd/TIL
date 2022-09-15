from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, T, M = map(int, input().split())
item_list = list(map(int, input().split()))
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((t, b))
    matrix[b].append((t, a))
max_cnt = 0
for i in range(N):
    start = []
    visited = [INF] * N
    heappush(start, [0, i])
    visited[i] = 0
    while start:
        x, node = heappop(start)
        if x > visited[node]:
            continue
        for k, v in matrix[node]:
            nx = x + k
            if visited[v] > nx:
                visited[v] = nx
                heappush(start, [nx, v])
    cnt = 0
    for j in range(N):
        if T >= visited[j]:
            cnt += item_list[j]
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)
