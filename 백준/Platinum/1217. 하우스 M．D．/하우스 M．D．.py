import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

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

while True:
    M, N = map(int, input().split())
    if (M, N) == (0, 0):
        break
    matrix = [[] for _ in range(2 * N + 1)]
    rev_matrix = [[] for _ in range(2 * N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        matrix[-a].append(b)
        matrix[-b].append(a)
        rev_matrix[b].append(-a)
        rev_matrix[a].append(-b)
    visited = [False] * (2 * N + 1)
    stack = []
    for i in range(1, 2 * N + 1):
        if not visited[i]:
            dfs(i)
    
    scc = [-1] * (2 * N + 1)
    cnt = 0
    while stack:
        node = stack.pop()
        if scc[node] == -1:
            rev_dfs(node)
            cnt += 1
    for i in range(1, N + 1):
        if scc[i] == scc[-i]:
            print(0)
            break
    else:
        print(1)