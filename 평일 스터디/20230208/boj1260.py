from collections import deque
N, M, start = map(int, input().split())
matrix = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited =[False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
for i in range(N+1):
    matrix[i].sort()    
dfs_visited[start] = 1
def dfs(start):
    print(start, end = ' ')
    dfs_visited[start]=True
    for i in matrix[start]:
        if not dfs_visited[i]:
            dfs(i)
def bfs(start):
    bfs_visited[start] = True
    start = deque([start])
    while start:
        x = start.popleft()
        print(x, end = ' ')
        for i in matrix[x]:
            if not bfs_visited[i]:
                start.append(i)
                bfs_visited[i] = True
dfs(start)
print()
bfs(start)