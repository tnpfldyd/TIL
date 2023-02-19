import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N, M = map(int, input().split())
initial = [0] + list(map(int, input().strip().split()))
switch = [[] for _ in range(N + 1)]
matrix = [[] for _ in range(2 * M + 1)]
rev_matrix = [[] for _ in range(2 * M + 1)]

def edge(x, y):
    matrix[x].append(y)
    rev_matrix[y].append(x)

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

for i in range(1, M + 1):
    switch_list = list(map(int, input().strip().split()))
    for j in range(1, switch_list[0] + 1):
        switch[switch_list[j]].append(i)

for i in range(1, N + 1):
    a, b = switch[i][0], switch[i][1]
    if initial[i]:
        edge(a, b); edge(b, a); edge(-a, -b); edge(-b, -a)
    else:
        edge(-a, b); edge(a, -b); edge(-b, a); edge(b, -a)
visited = [False] * (2 * M + 1)
stack = []
for i in range(1, 2 * M + 1):
    if not visited[i]:
        dfs(i)

scc = [-1] * (2 * M + 1)
cnt = 0
while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_dfs(node)
        cnt += 1

for i in range(1, M + 1):
    if scc[i] == scc[-i]:
        print(0)
        break
else:
    print(1)
