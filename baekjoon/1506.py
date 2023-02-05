import sys
input = sys.stdin.readline
N = int(input())
cost_list = list(map(int, input().strip().split()))
board = [list(map(int, input().strip())) for _ in range(N)]
matrix = [[] for _ in range(N)]
rev_matrix = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j]:
            matrix[i].append(j)
            rev_matrix[j].append(i)

def dfs(node):
    visited[node] = True
    for next in matrix[node]:
        if not visited[next]:
            dfs(next)
    stack.append(node)

stack = []
visited = [False] * N
for i in range(N):
    if not visited[i]:
        dfs(i)

visited = [False] * N

def rev_dfs(node):
    visited[node] = True
    ret = cost_list[node]
    for next in rev_matrix[node]:
        if not visited[next]:
            ret = min(ret, rev_dfs(next))
    return ret
answer = 0
while stack:
    x = stack.pop()
    if not visited[x]:
        answer += rev_dfs(x)
print(answer)