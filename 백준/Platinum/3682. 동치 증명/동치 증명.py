import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
T = int(input())
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
    for i in rev_matrix[x]:
        if scc[i] == -1:
            rev_dfs(i)
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [[] for _ in range(N)]
    rev_matrix = [[] for _ in range(N)]
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
    scc = [-1] * N
    cnt = 0
    while stack:
        node = stack.pop()
        if scc[node] == -1:
            rev_dfs(node)
            cnt += 1
    if cnt == 1:
        print(0)
        continue

    in_degree = [0] * cnt
    out_degree = [0] * cnt
    for i in range(N):
        for j in matrix[i]:
            if scc[i] != scc[j]:
                in_degree[scc[j]] += 1
                out_degree[scc[i]] += 1
    l, r = 0, 0
    for i in range(cnt):
        if not in_degree[i]:
            l += 1
        if not out_degree[i]:
            r += 1
    print(max(l, r))
