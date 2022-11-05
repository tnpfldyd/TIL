from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K, S = map(int, input().split())
normal, hard = map(int, input().split())
start = deque()
K_list = [int(input())-1 for _ in range(K)]
load = [[] for _ in range(N)]
load_temp = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    load[a].append(b)
    load[b].append(a)
    load_temp.append((a, b))
visited = [False] * N
zombie = [False] * N
for i in K_list:
    visited[i] = True
    zombie[i] = True
    start.append((i, 0))
while start:
    node, cnt = start.popleft()
    for k in load[node]:
        if not visited[k] and cnt < S:
            visited[k] = True
            start.append((k, cnt+1))
matrix = [[] for _ in range(N)]
for a, b in load_temp:
    if not zombie[a] and not zombie[b]:
        if visited[b]:
            matrix[a].append((hard, b))
        else:
            matrix[a].append((normal, b))
        if visited[a]:
            matrix[b].append((hard, a))
        else:
            matrix[b].append((normal, a))
        if a == N-1:
            matrix[b].append((0, a))
        if b == N-1:
            matrix[a].append((0, b))
start = []
heappush(start, [0, 0])
cost = [INF] * N
cost[0] = 0
while start:
    x, node = heappop(start)
    if x > cost[node]:
        continue
    for k, v in matrix[node]:
        nx = x + k
        if cost[v] > nx:
            cost[v] = nx
            heappush(start, [nx, v])
print(cost[N-1])