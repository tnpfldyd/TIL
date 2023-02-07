from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10 ** 7)

def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for i in matrix[x]:
        if not visited[i]:
            dfs(i)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    if cnt not in depth:
        depth[cnt] = 1
    else:
        depth[cnt] += 1
    for i in rev_matrix[x]:
        if scc[i] == -1:
            rev_dfs(i)

N, M, S, T = map(int, input().split())
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]
S -= 1; T -= 1

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    rev_matrix[b].append(a)

visited = [False] * N
stack = []

for i in range(N):
    if not visited[i]:
        dfs(i)

cnt = 0
scc = [-1] * N
depth = {}
while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_dfs(node)
        cnt += 1

scc_adj = [[] for _ in range(cnt)]

for i in range(N):
    for j in matrix[i]:
        if scc[i] != scc[j]:
            scc_adj[scc[i]].append(scc[j])

if S == T:
    print(depth[scc[T]])
    
else:
    visited = [0] * cnt
    visited[scc[S]] = depth[scc[S]]
    start = deque()
    start.append(scc[S])
    while start:
        x = start.popleft()
        if x == scc[T]:
            continue
        for i in scc_adj[x]:
            nx = visited[x] + depth[i]
            if visited[i] < nx:
                visited[i] = nx
                start.append(i)
    print(visited[scc[T]])