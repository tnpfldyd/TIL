import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
rev_matrix = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    rev_matrix[b].append(a)

stack = []
visited = [False] * (N+1)
def dfs(node):
    visited[node] = True
    for next in matrix[node]:
        if not visited[next]:
            dfs(next)
    stack.append(node)

def rev_dfs(node):
    visited[node] = True
    ssc.append(node)
    for next in rev_matrix[node]:
        if not visited[next]:
            rev_dfs(next)
            
for node in range(1, N+1):
    if not visited[node]:
        dfs(node)
result = []
visited = [False] * (N+1)
while stack:
    ssc = []
    node = stack.pop()
    if not visited[node]:
        rev_dfs(node)
        result.append(sorted(ssc) + [-1])
result.sort()
print(len(result))
for i in result:
    print(*i)