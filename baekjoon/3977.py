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

def rev_dfs(node, cur):
    scc[node] = cur
    for next in rev_matrix[node]:
        if not scc[next]:
            rev_dfs(next, cur)

for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[] for _ in range(N)]
    rev_matrix = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        matrix[a].append(b)
        rev_matrix[b].append(a)
    visited = [False] * N
    stack = [] 
    for i in range(N):
        if not visited[i]:
            dfs(i)
    scc = [0] * N
    cnt = 1
    while stack:
        x = stack.pop()
        if not scc[x]:
            rev_dfs(x, cnt)
            cnt += 1
    in_degree = [0] * cnt
    for i in range(N):
        for j in matrix[i]:
            if scc[i] != scc[j]:
                in_degree[scc[j]] += 1
    scc_cnt, answer = -1, 0
    for i in range(1, cnt):
        if not in_degree[i]:
            scc_cnt += 1
            answer = i
    if scc_cnt:
        print('Confused')
    else:
        for i in range(N):
            if scc[i] == answer:
                print(i)
    if t != T:
        input()
        print()