import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

def dfs(cur, cost):
    global max_cost, u
    visited[cur] = cost
    if visited[cur] > max_cost:
        max_cost = visited[cur]
        u = cur
    for next_node, next_cost in matrix[cur]:
        if visited[next_node] != INF:
            continue
        dfs(next_node, cost + next_cost)


N = int(input())
matrix = [[] for _ in range(N + 1)]
for i in range(N - 1):
    x, y, z = map(int, input().split())
    matrix[x].append((y, z))
    matrix[y].append((x, z))

visited = [INF] * (N + 1)
max_cost = 0
u = 1
dfs(1, 0)

v = u
max_cost = 0
visited = [INF] * (N + 1)
dfs(v, 0)

result = visited[:]
visited = [INF] * (N + 1)
dfs(u, 0)

for i in range(1, N + 1):
    print(max(result[i], visited[i]))