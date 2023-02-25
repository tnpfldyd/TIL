from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
input = map(int, sys.stdin.read().split())

def dfs(x):
    visited[x] = True
    for next in matrix[x]:
        if not visited[next]:
            dfs(next)
    stack.append(x)

def rev_dfs(x):
    scc[x] = cnt
    scc_edges[cnt].append(x)
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)

while True:
    N = next(input)
    if not N:
        break
    M = next(input)
    matrix = [[] for _ in range(N)]
    rev_matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b = next(input), next(input)
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
    scc_edges = defaultdict(list)
    while stack:
        node = stack.pop()
        if scc[node] == -1:
            rev_dfs(node)
            cnt += 1
    out_degree = [0] * cnt
    for i in range(N):
        for j in matrix[i]:
            if scc[i] != scc[j]:
                out_degree[scc[i]] += 1
    answer = []
    for i in range(cnt):
        if not out_degree[i]:
            for j in scc_edges[i]:
                answer.append(j + 1)
    answer.sort()
    print(*answer)