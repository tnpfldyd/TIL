import sys
input = sys.stdin.readline

def dfs(node, cnt):
    global answer
    visited[node] = True
    if cnt == 4:
        answer = True
        return 
    for next in matrix[node]:
        if not visited[next] and not answer:
            dfs(next, cnt+1)
    visited[node] = False

N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
answer = False
visited = [False] * N
for i in range(N):
    if answer:
        break
    dfs(i, 0)
print(1 if answer else 0)