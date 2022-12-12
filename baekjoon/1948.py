from collections import deque
import sys
input = sys.stdin.readline
N, M = int(input()), int(input())
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]
in_degree = [0] * N
cost_list = [0] * N
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1 ; b -= 1
    matrix[a].append((t, b))
    rev_matrix[b].append((t, a))
    in_degree[b] += 1
S, E = map(int, input().split())
S -= 1; E -= 1
start = deque()
start.append((0, S))
while start:
    cost, node = start.popleft()
    if cost < cost_list[node]:
        continue
    for k, v in matrix[node]:
        nx = cost + k
        if cost_list[v] < nx:
            cost_list[v] = nx
        in_degree[v] -= 1
        if not in_degree[v]:
            start.append((cost_list[v], v))
cnt = 0
start.append((cost_list[v], E))
visited = [False] * N
visited[E] = True
while start:
    cost, node = start.popleft()
    for k, v in rev_matrix[node]:
        if cost - k == cost_list[v]:
            cnt += 1
            if not visited[v]:
                visited[v] = True
                start.append((cost_list[v], v))
print(cost_list[E])
print(cnt)