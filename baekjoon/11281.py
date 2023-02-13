import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, M = map(int, input().split())
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
def dfs(x):
    visited[x] = True
    for next in matrix[x]:
        if not visited[next]:
            dfs(next)
    stack.append(x)

for i in range(1, 2 * N + 1):
    if not visited[i]:
        dfs(i)

scc = [-1] * (2 * N + 1)
cnt = 0

def rev_dfs(x):
    scc[x] = cnt
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)

while stack:
    x = stack.pop()
    if scc[x] == -1:
        rev_dfs(x)
        cnt += 1

for i in range(1, N + 1):
    if scc[i] == scc[-i]:
        print(0)
        break
else:
    print(1)
    for i in range(1, N + 1):
        if scc[i] < scc[-i]:
            print(0, end=' ')
        else:
            print(1, end=' ')