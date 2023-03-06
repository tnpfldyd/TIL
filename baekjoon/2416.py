import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
M, N = map(int, input().split())
matrix = [[] for _ in range(2 * N + 1)]
rev_matrix = [[] for _ in range(2 * N + 1)]

def add_edge(x, y):
    matrix[-x].append(y)
    matrix[-y].append(x)
    rev_matrix[y].append(-x)
    rev_matrix[x].append(-y)

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
    
for _ in range(M):
    a, q1, b, q2 = map(int, input().split())
    a = a if q1 else -a
    b = b if q2 else -b
    add_edge(a, b)


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
        print('IMPOSSIBLE')
        break
else:
    for i in range(1, N + 1):
        if scc[i] > scc[-i]:
            print(1)
        else:
            print(0)