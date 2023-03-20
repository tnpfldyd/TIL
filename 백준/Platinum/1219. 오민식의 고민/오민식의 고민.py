from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, S, E, M = map(int, input().split())

matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    matrix[a].append((cost, b))
money = list(map(int, input().split()))

dist = [INF] * N
dist[S] = -money[S]
stack = deque()
visited = [False] * N
for i in range(1, N + 1):
    for cur in range(N):
        for next_cost, next_node in matrix[cur]:
            new_cost = next_cost + dist[cur] - money[next_node]
            if dist[cur] != INF and dist[next_node] > new_cost:
                dist[next_node] = new_cost
                if i == N:
                    visited[cur] = True
                    stack.append(cur)
if dist[E] == INF:
    print('gg')
else:
    while stack:
        cur = stack.popleft()
        for next_cost, next_node in matrix[cur]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
    print('Gee' if visited[E] else -dist[E])