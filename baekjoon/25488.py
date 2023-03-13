import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    matrix = [[] for _ in range(N + 1)]
    rev_matrix = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        if c == 1:
            matrix[a].append(b)
            rev_matrix[b].append(a)
        else:
            matrix[a].append(b)
            matrix[b].append(a)
            rev_matrix[a].append(b)
            rev_matrix[b].append(a)

    def dfs(x):
        visited[x] = True
        for next_node in matrix[x]:
            if not visited[next_node]:
                dfs(next_node)
        stack.append(x)

    def rev_dfs(x):
        scc[x] = cnt
        for next_node in rev_matrix[x]:
            if scc[next_node] == -1:
                rev_dfs(next_node)

    stack = []
    visited = [False] * (N + 1)

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
    print(1 if cnt == 1 else 0)
