import sys
#sys.stdin = open('link.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N + 1):
    graph.append([])

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
cnt = 0

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)