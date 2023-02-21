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
    rev_stack.append(x)
    for next in rev_matrix[x]:
        if scc[next] == -1:
            rev_dfs(next)

N, M = int(input()), int(input())
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append(b)
    rev_matrix[b].append(a)

stack = []
visited = [False] * N

for i in range(N):
    if not visited[i]:
        dfs(i)

scc = [-1] * N
cnt = 0
answer = 0
while stack:
    node = stack.pop()
    if scc[node] == -1:
        rev_stack = []
        rev_dfs(node)
        cnt += 1
        answer = max(answer, len(rev_stack))
print(answer)