import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    rev_matrix[b].append(a)

stack = []
visited = [False] * N
def dfs(node):
    visited[node] = True
    for next in matrix[node]:
        if not visited[next]:
            dfs(next)
    stack.append(node)
for i in range(N):
    if not visited[i]:
        dfs(i)

visited = [False] * N
result = []
def rev_dfs(node):
    visited[node] = True
    temp.append(node)
    for next in rev_matrix[node]:
        if not visited[next]:
            rev_dfs(next)
while stack:
    x = stack.pop()
    temp = []
    if not visited[x]:
        rev_dfs(x)
        result.append(temp)
print('Yes' if len(result) == 1 else 'No')