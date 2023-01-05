import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, start = map(int, input().rstrip().split())
result = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().rstrip().split())
    result[a].append(b)
    result[b].append(a)
for i in range(N+1):
    result[i].sort()
visited[start] = 1
cnt = 1
def dfs(start):
    global cnt
    if visited[start] == 0:
        cnt += 1
        visited[start] = cnt
    for i in result[start]:
        if visited[i] == 0:
            dfs(i)
dfs(start)
for i in range(1, N+1):
    print(visited[i])