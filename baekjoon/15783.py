import sys, copy
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)

def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    for next in matrix[node]:
        if not visited[next]:
            dfs(next)
    stack.append(node)
visited = [False] * N
stack = []
for i in range(N):
    if not visited[i]:
        dfs(i)
check = copy.deepcopy(stack)
visited = [False] * N
cnt = 0
while check:
    x = check.pop()
    if not visited[x]:
        cnt += 1
        dfs(x)
print(cnt)