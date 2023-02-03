import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
T = int(input())
def dfs(node):
    visited[node] = True
    for next in matrix[node]:
        if not visited[next]:
            dfs(next)
    stack.append(node)

def rev_dfs(node):
    visited[node] = True
    scc[node] = idx
    temp.append(node)
    for next in rev_matrix[node]:
        if not visited[next]:
            rev_dfs(next)
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [[] for _ in range(N)]
    rev_matrix = [[] for _ in range(N)]
    visited = [False] * N
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        matrix[a].append(b)
        rev_matrix[b].append(a)
    stack = []
    for i in range(N):
        if not visited[i]:
            dfs(i)
    visited = [False] * N
    result = []
    idx = 0
    scc = [-1] * N
    while stack:
        x = stack.pop()
        temp = []
        if not visited[x]:
            rev_dfs(x)
            idx += 1
            result.append(sorted(temp))
    indegree = [0] * idx
    for i in range(N):
        for next in matrix[i]:
            if scc[i] != scc[next]:
                indegree[scc[next]] += 1
    cnt = 0
    for i in range(idx):
        if not indegree[i]:
            cnt += 1
    print(cnt)