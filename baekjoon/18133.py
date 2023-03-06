import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
rev_matrix = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    rev_matrix[b].append(a)

def dfs(x):
    visited[x] = True
    for next in matrix[x]:
        if not visited[next]:
            dfs(next)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)

visited = [False] * (N + 1)
stack = []
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

scc = [-1] * (N + 1)
cnt = 0
while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_dfs(node)
        cnt += 1
indegree = [0] * cnt

for i in range(1, N + 1):
    for next in matrix[i]:
        if scc[i] != scc[next]:
            indegree[scc[next]] += 1
answer = 0
for i in range(cnt):
    if not indegree[i]:
        answer += 1
print(answer)