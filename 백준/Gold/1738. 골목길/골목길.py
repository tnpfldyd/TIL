from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
edges = []
rev_graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
dist = [INF] * (N + 1)
visit = [False] * (N + 1)
cycle = False

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, -w))
    rev_graph[v].append(u)

dist[1] = 0

q = deque([N])
visit[N] = True
while q:
    cidx = q.popleft()
    for next in rev_graph[cidx]:
        if not visit[next]:
            visit[next] = True
            q.append(next)

for i in range(1, N+1):
    for b, a, cost in edges:
        if dist[b] == INF:
            continue
        if dist[a] > dist[b] + cost:
            if i == N and visit[b]:
                cycle = True
            dist[a] = dist[b] + cost
            parent[a] = b

def find_route():
    trace = []
    current = N
    while current:
        trace.append(current)
        current = parent[current]
    return ' '.join(map(str, trace[::-1]))

print(-1 if cycle else find_route())