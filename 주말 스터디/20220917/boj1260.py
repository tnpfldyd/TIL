from collections import deque
N, M, start = map(int, input().split())
stack = [[] for _ in range(N+1)]
stack_visited = [False] * (N+1)
dec_visited =[False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    stack[a].append(b)
    stack[b].append(a)
for i in range(N+1):
    stack[i].sort()    
stack_visited[start] = 1
def dfs(start):
    print(start, end = ' ')
    stack_visited[start]=True
    for i in stack[start]:
        if not stack_visited[i]:
            dfs(i)
def bfs(start):
    dec_visited[start] = True
    d = deque([start])
    while d:
        x = d.popleft()
        print(x, end = ' ')
        for i in stack[x]:
            if not dec_visited[i]:
                d.append(i)
                dec_visited[i] = True
dfs(start)
print()
bfs(start)