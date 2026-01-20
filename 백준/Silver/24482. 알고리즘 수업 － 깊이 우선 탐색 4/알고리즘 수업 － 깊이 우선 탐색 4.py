import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

depth = [-1] * (N + 1)

def dfs(cur, d):
    depth[cur] = d
    for nxt in graph[cur]:
        if depth[nxt] == -1:
            dfs(nxt, d + 1)

dfs(R, 0)

for i in range(1, N + 1):
    print(depth[i])